#!/usr/bin/python3
"""
A script that takes in the request of a URL, send a request to it and,
displays the value of X-Request-Id variable found in the header of response
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
