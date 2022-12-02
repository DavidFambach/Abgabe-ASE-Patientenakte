from .startup import start
from django.apps import AppConfig

start()

class FileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_file'
