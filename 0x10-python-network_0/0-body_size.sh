#!/usr/bin/bash
# A bash script that takes in URL, send a request to the  URL,
# and display the size of the of body of the response
curl -s "$1" | wc -c
