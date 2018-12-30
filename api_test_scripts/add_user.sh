#!/bin/bash
# Development testing script
# Note: admin privileges are required to add a user 
USER=$1
EMAIL="$USER@test.com"


curl -i \
-u admin2:somepasswd \
-H "Content-Type: application/json" \
-X POST --data '{"email": "'"$EMAIL"'", "password": "notsecret", "username": "'"$USER"'"}' http://127.0.0.1:8000/users/api/

