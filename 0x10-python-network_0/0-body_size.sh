#!/bin/bash
# A bash script that displays the size of the of body of the response
curl -s "$1" | wc -c
