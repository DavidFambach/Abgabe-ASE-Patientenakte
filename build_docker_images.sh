#!/usr/bin/env bash

echo Building images for project Patientenakte
echo Note: Any images which are already present, as identified by their docker image tag, will NOT be rebuilt
echo
echo

cd "$(dirname "$0")"

if [ $(docker image ls | grep "^patientenakte-auth_api " | wc -l) -gt 0 ]; then
	echo Authentication service image is already present. Skipping build.
else
	echo Building authentication service
	cp "./Konfiguration/Signature Key Pair/jwt-signature-rsa-private.pem" ./Authentifizierungsdienst/config/
	cp "./Konfiguration/Signature Key Pair/jwt-signature-rsa-public.pem" ./Authentifizierungsdienst/config/
	docker build -t patientenakte-auth_api ./Authentifizierungsdienst
fi

if [ $(docker image ls | grep "^patientenakte-file_api " | wc -l) -gt 0 ]; then
	echo File service image is already present. Skipping build.
else
	echo Building file service
	cp "./Konfiguration/Signature Key Pair/jwt-signature-rsa-public.pem" ./Dateiverwaltungsdienst/config/
	docker build -t patientenakte-file_api ./Dateiverwaltungsdienst
fi

if [ $(docker image ls | grep "^patientenakte-ssl-enabled-postgres " | wc -l) -gt 0 ]; then
	echo Postgres with TLS image is already present. Skipping build.
else
	echo Building Postgres with TLS
	docker build -t patientenakte-ssl-enabled-postgres -f ./Konfiguration/Dockerfiles/ssl-enabled-postgres.txt ./Konfiguration/Dockerfiles
fi

if [ $(docker image ls | grep "^patientenakte-bff " | wc -l) -gt 0 ]; then
	echo Webserver image is already present. Skipping build.
else
	
	if [ $(docker image ls | grep "^patientenakte-build-frontend " | wc -l) -gt 0 ]; then
		echo Frontend build utility image is already present. Skipping build.
	else
		echo Building frontend build utility
		docker build -t patientenakte-build-frontend -f ./Konfiguration/Dockerfiles/frontend-build-environment.txt ./Konfiguration/Dockerfiles
	fi
	
	echo Building webserver
	
	docker create -i --name patientenakte-build-frontend patientenakte-build-frontend
	
	# Cannot exclude from docker cp; need to include explicitly
	docker cp ./Webserver/frontend/public patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/src patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/babel.config.js patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/jsconfig.json patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/package.json patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/package-lock.json patientenakte-build-frontend:/frontend-project/frontend/
	docker cp ./Webserver/frontend/vue.config.js patientenakte-build-frontend:/frontend-project/frontend/

	docker start patientenakte-build-frontend
	docker attach patientenakte-build-frontend
	docker stop patientenakte-build-frontend
	rm -R ./Webserver/static
	docker cp patientenakte-build-frontend:/frontend-project/frontend/dist ./Webserver/static
	docker container rm patientenakte-build-frontend
	
	docker build -t patientenakte-bff ./Webserver
	
fi
