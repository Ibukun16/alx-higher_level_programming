#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    quest = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(quest.text)))
    print("\t- content: {}".format(quest.text))
