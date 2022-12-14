import __main__
import manage
import os

from .messaging import start_listener

IS_DJANGO_SERVER = __main__.__file__ == manage.__file__

def start():
    if IS_DJANGO_SERVER and "DJANGO_PARENT_PROCESS" not in os.environ:
        os.environ["DJANGO_PARENT_PROCESS"] = str(os.getpid())
        return
    _on_startup()

def _on_startup():
    start_listener()
