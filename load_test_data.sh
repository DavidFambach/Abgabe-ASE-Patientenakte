#!/usr/bin/env bash

echo Loading test data for project Patientenakte
echo
echo This script can be used to load example data into the databases of the running application, thereby providing a simple way to populate the initially empty database. It is, however, not required that the database is empty when loading the test data. In this case, the test data will be added. Do note that loading test data uses predefined values which may replace existing data. Furthermore, this operation may skip checks which are executed during the natural insertion of the data.
echo This operation may leave the application in an broken or unsafe state.
read -n 1 -rp "Do you want to continue [y/N]"
echo
if [ "$REPLY" == "y" -o "$REPLY" == "Y" ]; then
	echo
	echo
else
	echo Abort.
	exit 1
fi

cd "$(dirname "$0")"

docker logs -n 0 patientenakte-auth-api &> /dev/null
if [ $? -eq 0 ]; then
	docker cp ./Authentifizierungsdienst/authentication/fixtures patientenakte-auth-api:/code/authentication/fixtures
	docker exec patientenakte-auth-api python3 manage.py loaddata TestUser | sed -e "s/^/>> /"
	echo
	echo Test user has been added to the user database:
	echo "  User ID: 1"
	echo "  E-Mail: max@mustermann.de"
	echo "  Password: Mu5TerPassW0rt!"
	echo
else
	echo Authentication service is not active. No data for that service will be loaded.
fi

docker logs -n 0 patientenakte-file-api &> /dev/null
if [ $? -eq 0 ]; then
	docker cp ./Dateiverwaltungsdienst/app_file/fixtures patientenakte-file-api:/code/app_file/fixtures
	docker exec patientenakte-file-api python3 manage.py loaddata test_files | sed -e "s/^/>> /"
	echo
	echo Example data has been loaded for users with ID 1 and 2
	echo
else
	echo File service is not active. No data for that service will be loaded.
fi
