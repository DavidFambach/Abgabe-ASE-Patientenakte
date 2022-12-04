import subprocess

from threading import Thread

APP_NAME = "app_bff"
WSGI_APP_NAME = "bff.wsgi:application"

class RunnableThread(Thread):
    def __init__(self, r):
        super().__init__()
        self.r = r
    def run(self) -> None:
        self.r()

def _read_all(process):
    status = process.poll()
    while status is None:
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode("utf-8"))
        status = process.poll()

def _run_nginx():
    _read_all(subprocess.Popen(["nginx", "-g", "daemon off;"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))

if __name__ == "__main__":

    nginx_thread = RunnableThread(_run_nginx)
    nginx_thread.daemon = True
    nginx_thread.start()

    _read_all(subprocess.Popen(["python", "-m", "waitress", "--listen=*:8000", WSGI_APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
