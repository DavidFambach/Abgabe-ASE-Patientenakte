## docker setup
Prerequisite: Docker is installed on your current computer and the source code of the authentication service is available.
1. switch to the project path of the authentication service with the command line.
2. run docker compose up (restart the _auth_api_ container after installation if necessary)
3. switch to the _auth_api_ container with
   ```bash 
   docker exec -t -i <containerID> bash
   ```   
   (you can find out the _containerID_ with `docker ps`)
4. From the _/code_ directory, run 
    ```bash
    python manage.py migrate authentication
    python manage.py migrate
    python manage.py migrate --run-syncdb
    ```
Now the API is linked to the database and the database is prepared.

## run tests
to test the authentication service you need to have Docker Compose set up. Now you need to reconnect to the _auth_api_ (see docker setup 3.) and run from the _/code_ directory
```bash
python manage.py test
```