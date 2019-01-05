# Django Badger
Award Badges

## Example cURL commands to exercise the API
You can test the API from the command line using cURL. If you pipe the
response to json_pp it will format the returned data. 

### Add user
```bash
curl -i \
-u admin2:somepasswd \
-H "Content-Type: application/json" \
-X POST --data '{"email": "user@abc.com", "password": "notsecret", "username": "user1"}' http://localhost:8000/users/api/
```
### List users 
```bash
$ curl  -u fred:mypassword http://localhost:8000/users/api/ | json_pp
```

## Example Docker commands
You can run commands in Docker containers. Some examples are given below:

```bash
$ docker-compose exec web sh api_test_scripts/add_user.sh user1
```

```bash
$ docker-compose exec web ./manage.py makemigrations
$ docker-compose exec web ./manage.py migrate
```

## Prerequisites to run functional tests
The functional tests use the Firefox web browser and Geckodriver.

The Geckodriver is available from:

	 https://github.com/mozilla/geckodriver/releases.

You should download and extract it and put it somewhere on your system path,
for example, /usr/local/bin if running Linux.

