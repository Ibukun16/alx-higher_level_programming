#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to:
- http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    try:
        arg = sys.argv[1]
    except Exception:
        arg = ""
        q = {"q": arg}
    quest = requests.post(url, data=q)
    try:
        response = quest.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print(f"[{response["id"]}] {response["name"]}")
    except Exception:
        print("No result")
