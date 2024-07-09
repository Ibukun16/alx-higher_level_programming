#!/usr/bin/python3
"""
A Python script that takes in a URL,
- sends a request to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    quest = requests.get(url)
    if quest.status_code >= 400:
        print("Error code: {}".format(quest.status_code))
    else:
        print(quest.text)
