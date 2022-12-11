import logging
import requests

from django.conf import settings
from django.http import HttpRequest, HttpResponse, Http404
from django.views.static import serve
from typing import Union
from urllib.parse import urlencode
from urllib3.util import Url

ALLOWED_PROXY_METHODS = ["OPTIONS", "HEAD", "GET", "POST", "PUT", "DELETE"]
CLIENT_TO_PROXY_HEADERS = ["authorization", "content-type"]
PROXY_TO_CLIENT_HEADERS = ["content-type"]

class _ProxyConfiguration:
    def __init__(self, scheme: str, host: str, port: int, path: str, ca_certificate_path: Union[str, None]):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.path = path if path.endswith("/") else path + "/"
        self.ca_certificate_path = ca_certificate_path
    def handle(self, request: HttpRequest, path: str) -> HttpResponse:
        url = None
        try:
            if request.method not in ALLOWED_PROXY_METHODS:
                return HttpResponse(status=405)
            path = self.path + path
            url = Url(scheme=self.scheme, host=self.host, port=self.port, path=path, query=urlencode(request.GET))
            url = url.url
            headers = {header: value for header, value in request.headers.items() if header.lower() in CLIENT_TO_PROXY_HEADERS}
            response = requests.request(method=request.method, url=url, headers=headers, data=request.body, verify=self.ca_certificate_path)
            headers = {header: value for header, value in response.headers.items() if header.lower() in PROXY_TO_CLIENT_HEADERS}
            return HttpResponse(status=response.status_code, headers=headers, content=response.content)
        except Exception as e:
            logging.info("Proxy request to \"%s\" failed" % ("<none>" if url is None else url))
            logging.exception(e)
            raise Http404

def _parse_proxy_configuration(config: dict[str, str]) -> Union[_ProxyConfiguration, None]:
    if config is None:
        return None
    try:
        scheme = config["scheme"]
        host = config["host"]
        port = int(config["port"])
        path = config.get("path", "/")
        ca_certificate_path = config.get("certificate_path", None)
    except (KeyError, ValueError):
        return None
    if scheme is None or scheme == "" or host is None or host == "":
        return None
    if port <= 0 or port >= 65536:
        return None
    if path is None or path == "":
        path = "/"
    return _ProxyConfiguration(scheme, host, port, path, ca_certificate_path)
AUTHENTICATION_SERVICE: Union[_ProxyConfiguration, None] = _parse_proxy_configuration(settings.USED_SERVICES.get("authentication_service", None))
File_SERVICE: Union[_ProxyConfiguration, None] = _parse_proxy_configuration(settings.USED_SERVICES.get("file_service", None))
del _parse_proxy_configuration

def handle_proxy_authentication_service(request: HttpRequest, path: str) -> HttpResponse:
    if AUTHENTICATION_SERVICE is None:
        raise Http404()
    return AUTHENTICATION_SERVICE.handle(request, path)

def handle_proxy_file_service(request: HttpRequest, path: str) -> HttpResponse:
    if File_SERVICE is None:
        raise Http404()
    return File_SERVICE.handle(request, path)

def handle_static(request: HttpRequest, path: str, **kwargs) -> HttpResponse:
    if path in settings.ROOT_EQUIVALENT_PATHS:
        path = "index.html"
    elif path.endswith("/") or path == "":
        path = path + "index.html"
    return serve(request, path=path, document_root=settings.STATIC_ROOT, **kwargs)
