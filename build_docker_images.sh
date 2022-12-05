#!/usr/bin/env bash

# build the Docker image for the Authentifizierungsdienst
cd Authentifizierungsdienst
docker build -t patientenakte-auth_api .
cd ..

# build the Docker image for the Dateiverwaltungsdienst
cd Dateiverwaltungsdienst
docker build -t patientenakte-file_api .
cd ..

# build the Docker image for the frontend build
docker build -t patientenakte-build-frontend -f ./Konfiguration/Dockerfiles/frontend-build-environment.txt ./Konfiguration/Dockerfiles

# start a new Docker container from patientenakte-file_ap
# docker create -it --name patientenakte-build-frontend ubuntu sh -c "apt-get update && apt-get install npm -y && cd frontend-project && npm install && npm run build"
docker create -it --name patientenakte-build-frontend patientenakte-build-frontend

# copy the frontend project into the container
docker cp ./Webserver/frontend patientenakte-build-frontend:/frontend-project/

docker start patientenakte-build-frontend
docker attach patientenakte-build-frontend
docker stop patientenakte-build-frontend
# rm -R ./Webserver/static
docker cp patientenakte-build-frontend:/frontend-project/frontend/dist ./Webserver/static
docker container rm patientenakte-build-frontend

# build the Docker image for the Webserver
cd Webserver
docker build -t patientenakte-bff .
cd ..

