#!/bin/bash
# Need to be an admin to add a user
curl -u admin2:somepasswd -H "Content-Type: application/json" -X POST --data '{"email": "test1@test1.com", "password": "Xcy2bfgdds", "username": "test1"}' http://127.0.0.1:8000/users/api/

