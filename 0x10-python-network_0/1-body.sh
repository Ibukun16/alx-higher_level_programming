#!/usr/bin/bash
# A bash script that takes in a URL, sends a GET response to the URL
# and display the body of the 200 status code response
curl -sL "$1"
