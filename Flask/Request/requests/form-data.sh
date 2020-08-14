#!/bin/bash

curl --location --request POST 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=Spondon' \
--data-urlencode 'password=12345678'