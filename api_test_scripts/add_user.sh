#!/bin/bash
curl -u user:password -H "Content-Type: application/json" -X POST --data '{"email": "foo1@bar.com", "password": "foobar", "username": "foobar1"}' http://127.0.0.1:8000/users/api/

