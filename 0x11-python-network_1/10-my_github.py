#!/usr/bin/python3
"""
A Python script that takes my GitHub credentials (username and password),
and uses the GitHub API to display the id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    aut = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    quest = requests.get("https://api.github.com/user", aut)
    print(quest.json().get("id"))
