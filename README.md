# django_badger
Award badges to employees

## Curl commands to exercise API

You can test the API from the command line using cURL. If you pipe the
response to json_pp it will format the returned data. 

### List users 
```bash
$ curl  -u fred:mypassword http://127.0.0.1:8000/users/api/ | json_pp
```

## Prerequisites to run functional tests
The functional tests use the Firefox web browser and Geckodriver.

The Geckodriver is available from:

	 https://github.com/mozilla/geckodriver/releases.

You should download and extract it and put it somewhere on your system path,
for example, /usr/local/bin if running Linux.

