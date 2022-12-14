from . import views
from django.urls import re_path

USERINFO_VIEW = views.UserInfoView()
FILE_VIEW = views.FileView()
DIRECTORY_VIEW = views.DirectoryView()
SHARE_VIEW = views.ShareView()
CONTACT_VIEW = views.ContactView()

urlpatterns = [
    re_path(r"userinfo/(?P<user_id>[0-9]+)/?", USERINFO_VIEW.handle, name="Userinfo endpoint"),
    re_path(r"^file/(?P<file_id>[0-9]+)/?$", FILE_VIEW.handle, name="File endpoint"),
    re_path(r"file/?", FILE_VIEW.handle, name="File endpoint"),
    re_path(r"dir/(?P<directory_id>[0-9]+)/?", DIRECTORY_VIEW.handle, name="Directory endpoint"),
    re_path(r"dir/?", DIRECTORY_VIEW.handle, name="Directory endpoint"),
    re_path(r"share/(?P<share_id>[0-9]+)/?", SHARE_VIEW.handle, name="Share endpoint"),
    re_path(r"share/?", SHARE_VIEW.handle, name="Share endpoint"),
    re_path(r"contact/(?P<contact_id>[0-9]+)/?", CONTACT_VIEW.handle, name="Contact endpoint"),
    re_path(r"contact/?", CONTACT_VIEW.handle, name="Contact endpoint")
]
