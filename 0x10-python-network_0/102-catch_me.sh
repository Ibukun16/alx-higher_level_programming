#!/bin/bash
#Script that makes request to 0.0.0.0:5000/catch_me and server respond You got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_m
