import os
import psycopg2
import subprocess
import time

APP_NAME = "authentication"

def _read_all(process):
    status = process.poll()
    while status is None:
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode("utf-8"))
        status = process.poll()

if __name__ == "__main__":
    failures = 0
    while True:
        try:
            con = psycopg2.connect(host=os.environ["POSTGRES_HOST"], port=os.environ["POSTGRES_PORT"], dbname=os.environ["POSTGRES_DATABASE"], user=os.environ["POSTGRES_USERNAME"], password=os.environ["POSTGRES_PASSWORD"])
            con.close()
            break
        except:
            failures += 1
            if failures % 15 == 0:
                print("Database is not reachable")
            time.sleep(1)
    print("Database is up")

    _read_all(subprocess.Popen(["python", "manage.py", "makemigrations", APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", "manage.py", "migrate"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", "manage.py", "migrate", APP_NAME], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))
    _read_all(subprocess.Popen(["python", "manage.py", "runserver", "0.0.0.0:8000"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT))