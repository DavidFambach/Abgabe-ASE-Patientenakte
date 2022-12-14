import os
import pika
import psycopg2
import subprocess
import time

from threading import Thread

APP_NAME = "app_file"
MANAGEMENT_SCRIPT_NAME = "manage.py"
WSGI_APP_NAME = "fileservice.wsgi:application"

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

    failures = 0
    while True:
        try:
            con = psycopg2.connect(host=os.environ["POSTGRES_HOST"], port=os.environ["POSTGRES_PORT"], dbname=os.environ["POSTGRES_DATABASE"], user=os.environ["POSTGRES_USERNAME"], password=os.environ["POSTGRES_PASSWORD"])
            con.close()
            break
        except Exception:
            failures += 1
            if failures % 15 == 0:
                print("Database is not reachable")
            time.sleep(1)
    print("Database is up")

    failures = 0
    while True:
        try:
            credentials = pika.PlainCredentials(username=os.environ["USER_UPDATE_QUEUE_USERNAME"], password=os.environ["USER_UPDATE_QUEUE_PASSWORD"])
            con = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["USER_UPDATE_QUEUE_HOST"], port=int(os.environ["USER_UPDATE_QUEUE_PORT"]), credentials=credentials))
            con.close()
            break
        except Exception:
            failures += 1
            if failures % 15 == 0:
                print("Message queue not reachable")
            time.sleep(1)
    print("Message queue is up")

    nginx_thread = RunnableThread(_run_nginx)
    nginx_thread.daemon = True
    nginx_thread.start()

    _read_all(subprocess.Popen(["python", MANAGEMENT_SCRIPT_NAME, "makemigrations", APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", MANAGEMENT_SCRIPT_NAME, "migrate"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", MANAGEMENT_SCRIPT_NAME, "migrate", APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", "-m", "waitress", "--listen=*:8000", WSGI_APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
