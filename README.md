# motopp
# ! NOT DONE YET !
## Description
To run a local instance of the app, you need to have docker and docker-compose installed.
Then run:
```Bash
git clone
touch .env
```
Add the following to the .env file:
```Bash
SECRET_KEY=your_secret_key
MYSQL_HOST=your_mysql_localhost
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
```
Finally, run:
```Bash
docker-compose up --build -d
```
