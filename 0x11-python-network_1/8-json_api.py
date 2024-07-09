#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to:
- http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    quest = requests.post(url, data=payload)
    try:
        response = quest.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(reponse.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
