#!/bin/bash

curl --location --request POST 'http://127.0.0.1:5000/upload' \
--header 'enctype: multipart/form-data' \
--form 'profile_picture=@/Users/spondon/Pictures/Photo Booth Library/Pictures/Photo on 8-9-20 at 8.57 PM.jpg'