#!/bin/bash
#Script that display the response status code of request sent to URL as argument
curl -s -o /dev/null -w "%{http_code}" "$1"

