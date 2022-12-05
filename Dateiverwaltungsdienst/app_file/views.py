import json
import jwt
import logging
import re

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest, HttpResponse
from typing import Callable, List, Union

from .serializers import *

STATUS_OK = ("ok", 200)
STATUS_CREATED = ("ok", 201)
STATUS_BAD_REQUEST = ("malformed_request", 400)
STATUS_UNAUTHORIZED = ("unauthorized", 401)
STATUS_NOT_FOUND = ("not_found", 404)
STATUS_PERMISSION_DENIED = ("permission_denied", 403)
STATUS_DUPLICATE_NAME = ("duplicate_name", 409)
STATUS_TRANSFERRAL_REJECTED = ("transferral_rejected", 422)
STATUS_CYCLIC_DIRECTORY_TREE = ("cycle_detected", 409)
STATUS_UNMOVABLE_DIRECTORY = ("unmovable_directory", 422)
STATUS_DIRECTORY_NOT_EMPTY = ("not_empty", 422)
STATUS_INVALID_SHARE_SUBJECT = ("invalid_subject", 422)
STATUS_QUOTA_EXCEEDED = ("quota_exceeded", 422)
STAUTS_INTERNAL_ERROR = ("internal_error", 500)

AUTHORIZATION_HEADER_NAME = "Authorization"

CLAIM_USER_ID = "user_id"
CLAIM_USER_NAME = "user_name"

# TODO use randomized UUIDs rather than serial numbers for ids, because incremental IDs allow guessing the number of objects crated

class AbstractView:

    def handle(self, request: HttpRequest, **kwargs) -> HttpResponse:
        try:
            if request.method == "GET":
                return self._handle_get(request, **kwargs)
            elif request.method == "POST":
                return self._handle_post(request, **kwargs)
            elif request.method == "PUT":
                return self._handle_put(request, **kwargs)
            elif request.method == "DELETE":
                return self._handle_delete(request, **kwargs)
            else:
                raise _ErrorBadRequest("Unsupported method: %s" % request.method)
        except _ErrorBadRequest as e:
            return _response_for_json(STATUS_BAD_REQUEST, message=e.msg)
        except _ErrorUnauthorized:
            return _response_for_json(STATUS_UNAUTHORIZED)
        except _ErrorAccessDenied:
            return _response_for_json(STATUS_PERMISSION_DENIED)
        except _ErrorDuplicateName:
            return _response_for_json(STATUS_DUPLICATE_NAME)
        except _ErrorTransferralRejected:
            return _response_for_json(STATUS_TRANSFERRAL_REJECTED)
        except _ErrorCyclicDirectoryTree:
            return _response_for_json(STATUS_CYCLIC_DIRECTORY_TREE)
        except _ErrorUnmovableDirectory:
            return _response_for_json(STATUS_UNMOVABLE_DIRECTORY)
        except _ErrorDirectoryNotEmpty:
            return _response_for_json(STATUS_DIRECTORY_NOT_EMPTY)
        except _ErrorInvalidShareSubject:
            return _response_for_json(STATUS_INVALID_SHARE_SUBJECT)
        except _ErrorNotFound:
            return _response_for_json(STATUS_NOT_FOUND)
        except ObjectDoesNotExist:
            return _response_for_json(STATUS_NOT_FOUND)
        except BaseException as e:
            logging.exception(e)
            return _response_for_json(STAUTS_INTERNAL_ERROR)

    def _handle_get(self, request: HttpRequest, **kwargs):
        raise _ErrorBadRequest("Unsupported method: GET")
    def _handle_post(self, request: HttpRequest, **kwargs):
        raise _ErrorBadRequest("Unsupported method: POST")
    def _handle_put(self, request: HttpRequest, **kwargs):
        raise _ErrorBadRequest("Unsupported method: PUT")
    def _handle_delete(self, request: HttpRequest, **kwargs):
        raise _ErrorBadRequest("Unsupported method: DELETE")

class UserInfoView(AbstractView):

    def _handle_get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        user_id = _get_kwarg(kwargs, "user_id", converter=int)
        user, _ = _verify_authenticated(request, user_id)
        _verify_can_access(user_id, user, is_write=False)
        return _response_for_json(STATUS_OK, userinfo=serialize_user_info(user))

class FileView(AbstractView):

    def _handle_get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, ["file_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        file_id = _get_kwarg(kwargs, "file_id", converter=int)
        file = File.objects.get(id=file_id)
        _verify_can_access(user_id, file, is_write=False)

        return _response_for_binary(STATUS_OK, file.data)

    def _handle_post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, [])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        file_name = _get_query_param(request, "name", converter=str)
        parent_directory_id = _get_query_param(request, "parentDirectory", converter=int)
        parent_directory = Directory.objects.get(id=parent_directory_id)
        _verify_can_access(user_id, parent_directory, is_write=True)
        _verify_unique_names(file_name, parent_directory)

        # TODO check quota

        file = File.objects.create(name=file_name, owner=parent_directory.owner, parent_directory=parent_directory, data=request.body)

        return _response_for_json(STATUS_OK, file=serialize_file(file))

    def _handle_put(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, ["file_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        file_name = _get_query_param(request, "name", required=False, converter=str)
        parent_directory_id = _get_query_param(request, "parentDirectory", required=False, converter=int)
        write_body = _get_query_param(request, "writebody", required=False, converter=_get_converter_for_enum([""])) == ""
        if not write_body and len(request.body) > 0:
            raise _ErrorBadRequest("Cannot have a request body when not editing the file content")
        file_id = _get_kwarg(kwargs, "file_id", converter=int)
        file = File.objects.get(id=file_id)
        _verify_can_access(user_id, file, is_write=True)

        if file_name is not None or parent_directory_id is not None:
            current_dir = file.parent_directory
            _verify_can_access(user_id, current_dir, is_write=True)
            target_dir = current_dir
            if parent_directory_id is not None:
                target_dir = Directory.objects.get(id=parent_directory_id)
                _verify_can_access(user_id, target_dir, is_write=True)
                _verify_same_owner(file, current_dir, target_dir)
                if current_dir != target_dir:
                    file.parent_directory = target_dir
            if file_name is not None:
                file.name = file_name
            _verify_unique_names(file, target_dir)
        if write_body:
            # TODO verify quota
            file.data = request.body

        file.save()

        return _response_for_json(STATUS_OK, file=serialize_file(file))

    def _handle_delete(self, request: HttpRequest, **kwargs):
        _verify_kwargs(kwargs, ["file_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        file_id = _get_kwarg(kwargs, "file_id", converter=int)
        file = File.objects.get(id=file_id)
        _verify_can_access(user_id, file, is_write=True)
        parent_directory = file.parent_directory
        _verify_can_access(user_id, parent_directory, is_write=True)

        file.delete()

        return _response_for_json(STATUS_OK)

class DirectoryView(AbstractView):

    def _handle_get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, ["directory_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        directory_id = _get_kwarg(kwargs, "directory_id", converter=int)
        directory = Directory.objects.get(id=directory_id)
        _verify_can_access(user_id, directory, is_write=False)

        return _response_for_json(STATUS_OK, directory=serialize_directory(directory, include_children=True))

    def _handle_post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, [])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        directory_name = _get_query_param(request, "name", converter=str)
        parent_directory_id = _get_query_param(request, "parentDirectory", converter=int)
        parent_directory = Directory.objects.get(id=parent_directory_id)
        _verify_can_access(user_id, parent_directory, is_write=True)
        _verify_unique_names(directory_name, parent_directory)

        directory = Directory.objects.create(name=directory_name, owner=parent_directory.owner, parent=parent_directory)

        return _response_for_json(STATUS_OK, directory=serialize_directory(directory))

    def _handle_put(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, ["directory_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        directory_name = _get_query_param(request, "name", required=False, converter=str)
        parent_directory_id = _get_query_param(request, "parentDirectory", required=False, converter=int)
        directory_id = _get_kwarg(kwargs, "directory_id", converter=int)
        directory = Directory.objects.get(id=directory_id)
        _verify_can_access(user_id, directory, is_write=True)

        if directory_name is not None or parent_directory_id is not None:
            current_dir = directory.parent
            _verify_can_access(user_id, current_dir, is_write=True)
            target_dir = current_dir
            if parent_directory_id is not None:
                target_dir = Directory.objects.get(id=parent_directory_id)
                _verify_can_access(user_id, target_dir, is_write=True)
                _verify_movable(directory, target_dir)
                _verify_same_owner(directory, current_dir, target_dir)
                if current_dir != target_dir:
                    directory.parent = target_dir
            if directory_name is not None:
                directory.name = directory_name
            _verify_unique_names(directory, target_dir)

        directory.save()

        return _response_for_json(STATUS_OK, directory=serialize_directory(directory))

    def _handle_delete(self, request: HttpRequest, **kwargs):
        _verify_kwargs(kwargs, ["directory_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        directory_id = _get_kwarg(kwargs, "directory_id", converter=int)
        directory = Directory.objects.get(id=directory_id)
        _verify_can_access(user_id, directory, is_write=True)
        parent_directory = directory.parent
        if parent_directory is None:
            raise _ErrorUnmovableDirectory()
        _verify_can_access(user_id, parent_directory, is_write=True)
        cascade = _get_query_param(request, "cascade", required=False, converter=_get_converter_for_enum([""])) == ""
        if cascade:
            # TODO this needs to be guarded by a transaction
            to_delete_list = [directory]
            while len(to_delete_list) > 0:
                to_delete = to_delete_list.pop()
                children = to_delete.directory_set.all()
                if len(children) == 0:
                    for file in to_delete.file_set.all():
                        file.delete()
                    to_delete.delete()
                else:
                    to_delete_list += [to_delete] + list(children)
        else:
            _verify_empty(directory)
            directory.delete()

        return _response_for_json(STATUS_OK)

class ShareView(AbstractView):

    def _handle_get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, ["share_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        share_id = _get_kwarg(kwargs, "share_id", converter=int)
        share = Share.objects.get(id=share_id)
        _verify_can_access(user_id, share, is_write=False)

        return _response_for_json(STATUS_OK, share=serialize_share(share))

    def _handle_post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        _verify_kwargs(kwargs, [])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        user = StorageUser.objects.get(id=user_id)
        subject_id = _get_query_param(request, "subject", converter=int)
        subject = StorageUser.objects.get(id=subject_id)
        target_type = _get_query_param(request, "targetType", converter=_get_converter_for_enum(["file", "directory"]))
        target_id = _get_query_param(request, "targetID", converter=int)
        target = Directory.objects.get(id=target_id) if target_type == "directory" else File.objects.get(id=target_id)
        _verify_can_access(user_id, target, is_write=True)
        can_write = _get_query_param(request, "canWrite", required=False, converter=_get_converter_for_enum([""])) == ""

        if target.owner.id != user_id:
            raise _ErrorAccessDenied()
        if user_id == subject_id:
            raise _ErrorInvalidShareSubject()

        target_dict = {"target_directory" if target_type == "directory" else "target_directory": target}
        share = Share.objects.create(issuer=user, subject=subject, **target_dict, can_write=can_write)

        return _response_for_json(STATUS_OK, share=serialize_share(share))

    def _handle_delete(self, request: HttpRequest, **kwargs):
        _verify_kwargs(kwargs, ["share_id"])

        user_id = _get_query_param(request, "user", converter=int)
        _verify_authenticated(request, user_id)

        share_id = _get_kwarg(kwargs, "share_id", converter=int)
        share = Share.objects.get(id=share_id)
        _verify_can_access(user_id, share, is_write=True)

        share.delete()

        return _response_for_json(STATUS_OK)

class _ErrorBadRequest(Exception):
    def __init__(self, msg: str):
        self.msg = msg

class _ErrorUnauthorized(Exception):
    pass

class _ErrorAccessDenied(Exception):
    pass

class _ErrorNotFound(Exception):
    pass

class _ErrorTransferralRejected(Exception):
    pass

class _ErrorDuplicateName(Exception):
    pass

class _ErrorCyclicDirectoryTree(Exception):
    pass

class _ErrorUnmovableDirectory(Exception):
    pass

class _ErrorDirectoryNotEmpty(Exception):
    pass

class _ErrorInvalidShareSubject(Exception):
    pass

def _get_kwarg(kwargs: dict[str, Any], name: str, required=True, default=None, converter: Callable[[str], Any]=lambda x: x) -> Any:
    if name in kwargs:
        try:
            return converter(kwargs[name])
        except ValueError:
            raise _ErrorBadRequest("Malformed value for \"%s\"" % name)
    if required:
        raise _ErrorBadRequest("Missing value for \"%s\"" % name)
    return default

def _verify_kwargs(kwargs: dict[str, Any], valid_names: List[str]):
    for name in kwargs:
        if name not in valid_names:
            raise _ErrorBadRequest("Cannot have value for \"%s\"" % name)

def _get_query_param(req: HttpRequest, name: str, required=True, default=None, converter: Callable[[str], Any]=lambda x: x) -> Any:
    query_dict = req.GET
    if name in query_dict:
        try:
            return converter(query_dict[name])
        except ValueError:
            raise _ErrorBadRequest("Malformed value for query parameter \"%s\"" % name)
    if required:
        raise _ErrorBadRequest("Missing required query parameter \"%s\"" % name)
    return default

def _get_converter_for_enum(accepted_values: List[str], converter: Callable[[str], Any]=lambda x: x) -> Callable[[str], Any]:
    def res(x: str):
        if not x in accepted_values:
            raise ValueError(str(x) + " is not a permitted value")
        return converter(x)
    return res

def _verify_authenticated(req: HttpRequest, user_id: int) -> (StorageUser, dict[str, Any]):

    token = req.headers.get(AUTHORIZATION_HEADER_NAME, None)
    if token is None:
        raise _ErrorUnauthorized()
    regex = re.compile("^Bearer ([^ ]+)$")
    if regex.match(token) is None:
        raise _ErrorUnauthorized()
    token = regex.sub("\\1", token)

    try:
        token = jwt.decode(token, settings.SECRET_KEY, settings.SIMPLE_JWT["ALGORITHM"])
    except Exception as e:
        logging.info("An invalid token was supplied for user with ID %s" % user_id)
        raise _ErrorUnauthorized()

    claimed_user_id = token.get(CLAIM_USER_ID, None)
    if claimed_user_id is None:
        logging.info("Encountered a valid token with no user_id set")
        raise _ErrorUnauthorized()
    if claimed_user_id != user_id:
        logging.info("User with ID %s attempted to authenticate as user with ID %s" % (claimed_user_id, user_id))
        raise _ErrorUnauthorized()

    for key in [CLAIM_USER_NAME]:
        if key not in token:
            logging.info("Encountered a valid token for user with ID %s which is missing the required claim \"%s\"" % (user_id, key))
            raise _ErrorUnauthorized()

    with transaction.atomic():
        try:
            user = StorageUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            user = StorageUser.objects.create(id=user_id, display_name=token[CLAIM_USER_NAME])
            Directory.objects.create(name="root", owner=user, parent=None)
            logging.info("Created new user with ID %s and display name \"%s\"" % (user_id, token[CLAIM_USER_NAME]))

    return user, token

def _verify_can_access(user_id: int, obj: Union[StorageUser, File, Directory, Share], is_write: bool) -> None:
    if obj is None:
        return
    if not obj.can_access(user_id, False):
        logging.info("User %d attempted to read %s, but is lacking the permission to do so" % (user_id, obj))
        raise _ErrorNotFound()
    if is_write and not obj.can_access(user_id, True):
        logging.info("User %d attempted to write %s, but is lacking the permission to do so" % (user_id, obj))
        raise _ErrorAccessDenied()

def _verify_same_owner(*args: Union[File, Directory]) -> None:
    if len(args) <= 1:
        return
    owner = args[0].owner
    for e in args:
        if e.owner != owner:
            raise _ErrorTransferralRejected()

def _verify_unique_names(to_check: Union[str, File, Directory], dir: Directory) -> None:
    if type(to_check) == str:
        for e in [*dir.file_set.all(), *dir.directory_set.all()]:
            if e.name == to_check:
                raise _ErrorDuplicateName()
    else:
        for e in [*dir.file_set.all(), *dir.directory_set.all()]:
            if e != to_check and e.name == to_check.name:
                raise _ErrorDuplicateName()

def _verify_movable(to_check: Directory, target_dir: Directory) -> None:
    if to_check.parent is None:
        raise _ErrorUnmovableDirectory()
    # TODO if this check is not enforced by the database, this check needs to be guarded by a transaction
    while target_dir is not None:
        if to_check == target_dir:
            raise _ErrorCyclicDirectoryTree()
        target_dir = target_dir.parent

def _verify_empty(to_check: Directory):
    if len(to_check.file_set.all()) > 0 or len(to_check.directory_set.all()) > 0:
        raise _ErrorDirectoryNotEmpty()

def _response_for_json(status: [str, int], **kwargs) -> HttpResponse:
    return _create_json_response({
        "status": status[0],
        **kwargs
    }, status=status[1])

def _response_for_binary(status: [str, int], data: bytes) -> HttpResponse:
    return _create_binary_response(data, status[1], content_type="application/octet-stream")

def _create_json_response(json_object: dict[str, Any], status: int) -> HttpResponse:
    return _create_binary_response(bytes(json.dumps(json_object), "utf-8"), status, content_type="application/json")

def _create_binary_response(data: bytes, status: int, **kwargs) -> HttpResponse:
    return HttpResponse(data, status=status, **kwargs)
