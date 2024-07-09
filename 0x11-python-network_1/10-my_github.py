#!/usr/bin/python3
"""
A Python script that takes my GitHub credentials (username and password),
and uses the GitHub API to display the id.
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    info = (username, password)
    quest = requests.get(url, auth=info)
    status = quest.status_code

    if status == 200:
        print(quest.json()['id'])
    else:
        print("None")
