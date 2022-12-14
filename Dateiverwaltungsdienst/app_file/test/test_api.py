from django.core.exceptions import ObjectDoesNotExist

from app_file.models import StorageUser, File, Directory, Share
from django.test import Client, TestCase
from django.utils.http import urlencode

SETTINGS = {
    "SIMPLE_JWT": {
        "ALGORITHM": "HS256",
        "VERIFYING_KEY": "123456"
    }
}

# The timestamp 1970-01-01 00:00:00 UTC is assumed to lie in the past
# The timestamp 3000-01-01 12:00:00 UTC is assumed to lie in the future
AUTHORIZATION_HEADERS = {
    "USER_1": {
        "VALID": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjozMjUwMzcxOTYwMCwiaWF0IjowLCJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJ0ZXN0In0._worc88eXHXNEjYLqCE9VD3LEMiR23s5gXyDFmauyiQ",
        "BAD_SIGNATURE": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjozMjUwMzcxOTYwMCwiaWF0IjowLCJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJ0ZXN0In0.aworc88eXHXNEjYLqCE9VD3LEMiR23s5gXyDFmauyiQ",
        "BAD_TYPE": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoib3RoZXIiLCJleHAiOjMyNTAzNzE5NjAwLCJpYXQiOjAsInVzZXJfaWQiOjEsInVzZXJfbmFtZSI6InRlc3QifQ.ZXQQRKzIqPQSCjQx7siLWBo27gljFp5Qe8SeURrAZqU",
        "BAD_IAT": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjozMjUwMzcxOTYwMCwiaWF0IjozMjUwMzcxOTYwMCwidXNlcl9pZCI6MSwidXNlcl9uYW1lIjoidGVzdCJ9.cR_xEwRiQYSsuOrK11LttRBn04MR8Tv8cX6PtmXdJys",
        "EXPIRED": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjowLCJpYXQiOjAsInVzZXJfaWQiOjEsInVzZXJfbmFtZSI6InRlc3QifQ.v7SPuYD1Bnk-rJl3q0UdfqPfAHaoC_Xre1k7NAFiIVM",
        "MISSING_USER_ID": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjozMjUwMzcxOTYwMCwiaWF0IjowLCJ1c2VyX25hbWUiOiJ0ZXN0In0.knG4EVciMdvRaCVXG_rdZ6VaIN1S_tiHHqUsDofnLtw",
        "MISSING_TYPE": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjMyNTAzNzE5NjAwLCJpYXQiOjAsInVzZXJfaWQiOjEsInVzZXJfbmFtZSI6InRlc3QifQ.iZwbs1tNJd0vN-SZ4JMKm2LJhyqyIK4F00Ng78IDRD4",
        "MISSING_EXP": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjowLCJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJ0ZXN0In0.nwvfrMVeydsXaMcj9eAQqQohyHffoUcPLOPZpelrCmY"
    },
    "USER_2": {
        "VALID": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjozMjUwMzcxOTYwMCwiaWF0IjowLCJ1c2VyX2lkIjoyLCJ1c2VyX25hbWUiOiJ0ZXN0In0.MsaDi1otqgIF8GvxOG8f2LnIucpE59rceAxL7LkroAE"
    }
}

CONTENT_TYPE_JSON = "application/json"

ROUTE_USERINFO = "/userinfo/"
ROUTE_FILE = "/file/"
ROUTE_DIRECTORY = "/dir/"
ROUTE_SHARE = "/share/"
ROUTE_CONTACT = "/contact/"

class TestAuthentication(TestCase):

    fixtures = ["test_files"]

    def test_authenticated_with_valid_token(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("userinfo" in response_body)

    def test_create_new_file(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_FILE + "?" + urlencode({"user": 1, "name": "newfile", "parentDirectory": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("file" in response_body)
            self.assertTrue("id" in response_body["file"])
            new_id = response_body["file"]["id"]
            self.assertEqual(type(new_id), int)
            self.assertEqual(self._dict_from_model(File.objects.get(id=new_id), extra_removed_keys=["data"]), {"id": new_id, "owner_id": 1, "name": "newfile", "parent_directory_id": 1})

    def test_create_new_directory(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_DIRECTORY + "?" + urlencode({"user": 1, "name": "newdirectory", "parentDirectory": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("directory" in response_body)
            self.assertTrue("id" in response_body["directory"])
            new_id = response_body["directory"]["id"]
            self.assertEqual(type(new_id), int)
            self.assertEqual(self._dict_from_model(Directory.objects.get(id=new_id)), {"id": new_id, "owner_id": 1, "name": "newdirectory", "parent_id": 1})

    def test_create_new_share(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_SHARE + "?" + urlencode({"user": 1, "subject": 2, "targetType": "file", "targetID": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("share" in response_body)
            self.assertTrue("id" in response_body["share"])
            new_id = response_body["share"]["id"]
            self.assertEqual(type(new_id), int)
            self.assertEqual(self._dict_from_model(Share.objects.get(id=new_id)), {"id": new_id, "issuer_id": 1, "subject_id": 2, "target_file_id": 1, "target_directory_id": None, "can_write": False})

    def test_create_new_contact(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_2"]["VALID"])
            response = client.post(ROUTE_CONTACT + "1?" + urlencode({"user": 2}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("contact" in response_body)
            self.assertEqual(self._dict_from_model(StorageUser.objects.get(id=2).contacts.get(id=1)), {"id": 1, "display_name": "Testpatient"})

    def test_update_file(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.put(ROUTE_FILE + "1?" + urlencode({"user": 1, "name": "newname", "parentDirectory": 2, "writebody": ""}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("file" in response_body)
            self.assertEqual(self._dict_from_model(File.objects.get(id=1)), {"id": 1, "owner_id": 1, "name": "newname", "parent_directory_id": 2, "data": b""})

    def test_update_directory(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.put(ROUTE_DIRECTORY + "3?" + urlencode({"user": 1, "name": "newname", "parentDirectory": 2}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body["status"], "ok")
            self.assertTrue("directory" in response_body)
            self.assertEqual(self._dict_from_model(Directory.objects.get(id=3)), {"id": 3, "owner_id": 1, "name": "newname", "parent_id": 2})

    def test_delete_file(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_FILE + "1?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "ok"})
            self.assertRaises(ObjectDoesNotExist, lambda: File.objects.get(id=1))

    def test_delete_directory(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_DIRECTORY + "4?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "ok"})
            self.assertRaises(ObjectDoesNotExist, lambda: Directory.objects.get(id=4))

    def test_delete_share(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_SHARE + "1?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "ok"})
            self.assertRaises(ObjectDoesNotExist, lambda: Share.objects.get(id=1))

    def test_delete_contact(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_CONTACT + "2?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "ok"})
            self.assertRaises(ObjectDoesNotExist, lambda: StorageUser.objects.get(id=1).contacts.get(id=2))

    def test_authenticated_with_no_token(self):
        with self.settings(**SETTINGS):
            client = Client()
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_invalid_signature_token(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["BAD_SIGNATURE"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_signature_and_bad_type(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["BAD_TYPE"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_signature_and_bad_issuing_time(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["BAD_IAT"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_expired_token(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["EXPIRED"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_signature_idless_token(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["MISSING_USER_ID"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_token_without_expiry_timestamp(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["MISSING_EXP"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authenticated_with_valid_signature_token_for_other_user(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_2"]["VALID"])
            response = client.get(ROUTE_USERINFO + "1")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unauthorized"})

    def test_all_endpoints_authenticate(self):
        with self.settings(**SETTINGS):
            for get_response in [
                lambda c: c.get(ROUTE_USERINFO + "1"),
                lambda c: c.get(ROUTE_FILE + "1?" + urlencode({"user": 1})),
                lambda c: c.post(ROUTE_FILE + "?" + urlencode({"user": 1, "name": "newfile", "parentDirectory": 1})),
                lambda c: c.put(ROUTE_FILE + "1?" + urlencode({"user": 1, "name": "newname"})),
                lambda c: c.delete(ROUTE_FILE + "1?" + urlencode({"user": 1})),
                lambda c: c.get(ROUTE_DIRECTORY + "1?" + urlencode({"user": 1})),
                lambda c: c.post(ROUTE_DIRECTORY + "?" + urlencode({"user": 1, "name": "newdirectory", "parentDirectory": 1})),
                lambda c: c.put(ROUTE_DIRECTORY + "1?" + urlencode({"user": 1, "name": "newname"})),
                lambda c: c.delete(ROUTE_DIRECTORY + "1?" + urlencode({"user": 1})),
                lambda c: c.get(ROUTE_SHARE + "1?" + urlencode({"user": 1})),
                lambda c: c.post(ROUTE_SHARE + "?" + urlencode({"user": 1, "subject": 2, "targetType": "file", "targetID": 1})),
                lambda c: c.delete(ROUTE_SHARE + "1?" + urlencode({"user": 1})),
                lambda c: c.get(ROUTE_CONTACT + "2?" + urlencode({"user": 1})),
                lambda c: c.post(ROUTE_CONTACT + "2?" + urlencode({"user": 1})),
                lambda c: c.delete(ROUTE_CONTACT + "2?" + urlencode({"user": 1}))
            ]:
                client = Client()
                response = get_response(client)
                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
                response_body = response.json()
                self.assertEqual(response_body, {"status": "unauthorized"})

    def test_authorization_check(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_2"]["VALID"])
            response = client.get(ROUTE_FILE + "1?" + urlencode({"user": 2}))
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "not_found"})

    def test_write_on_read_only_share(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_2"]["VALID"])
            response = client.post(ROUTE_FILE + "?" + urlencode({"user": 2, "name": "newname", "parentDirectory": 3}))
            self.assertEqual(response.status_code, 403)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "permission_denied"})

    def test_write_file_with_duplicate_name(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_FILE + "?" + urlencode({"user": 1, "name": "Beispieldatei", "parentDirectory": 1}))
            self.assertEqual(response.status_code, 409)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "duplicate_name"})

    def test_move_root(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.put(ROUTE_DIRECTORY + "1?" + urlencode({"user": 1, "parentDirectory": 2}))
            self.assertEqual(response.status_code, 422)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unmovable_directory"})

    def test_delete_root(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_DIRECTORY + "1?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 422)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "unmovable_directory"})

    def test_move_to_circlic_directory_tree(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.put(ROUTE_DIRECTORY + "2?" + urlencode({"user": 1, "parentDirectory": 4}))
            self.assertEqual(response.status_code, 409)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "cycle_detected"})

    def test_delete_not_empty_directory_without_cascade(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.delete(ROUTE_DIRECTORY + "2?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 422)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "not_empty"})

    def test_create_share_for_self(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_SHARE + "?" + urlencode({"user": 1, "subject": 1, "targetType": "directory", "targetID": 1}))
            self.assertEqual(response.status_code, 422)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "invalid_subject"})

    def test_create_self_contact(self):
        with self.settings(**SETTINGS):
            client = Client(HTTP_AUTHORIZATION=AUTHORIZATION_HEADERS["USER_1"]["VALID"])
            response = client.post(ROUTE_CONTACT + "1?" + urlencode({"user": 1}))
            self.assertEqual(response.status_code, 422)
            self.assertEqual(response.headers["Content-Type"], CONTENT_TYPE_JSON)
            response_body = response.json()
            self.assertEqual(response_body, {"status": "invalid_contact"})

    @staticmethod
    def _dict_from_model(obj, extra_removed_keys=None):
        d = obj.__dict__
        for e in ["_state"] + ([] if extra_removed_keys is None else extra_removed_keys):
            del d[e]
        return d
