#!/bin/bash
#A script that send JSON POST to a URL and display the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
