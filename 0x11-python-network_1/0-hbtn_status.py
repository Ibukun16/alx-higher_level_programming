#!/usr/bin/python3
""" A python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    query = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(query) as response:
        bd_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bd_content)))
        print("\t- content: {}".format(bd_content))
        print("\t- utf8 content: {}".format(bd_content.decode('utf-8')))
