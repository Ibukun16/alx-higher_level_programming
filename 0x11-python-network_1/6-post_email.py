#!/usr/bin/python3
""" A Python script that:
- takes in a URL and an email address,
- sends a POST request to the passed URL with the email as a parameter,
- and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    obj = {"email": sys.argv[2]}

    quest = requests.post(url, data=obj)
    print(quest.txt)
