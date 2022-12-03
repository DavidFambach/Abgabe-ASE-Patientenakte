from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r"^auth/(?P<path>.*)$", views.handle_proxy_authentication_service, name="Authentication service"),
    re_path(r"^file/(?P<path>.*)$", views.handle_proxy_file_service, name="File service"),
    re_path(r"^(?P<path>.*)$", views.handle_static, name="Frontend resources")
]
