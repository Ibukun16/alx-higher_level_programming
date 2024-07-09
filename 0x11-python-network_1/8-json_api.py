#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to:
- http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    q = {"q": letter}
    quest = requests.post(url, data=q)
    try:
        response = quest.json()
        if response:
            print(f"[{response['id']}] {response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
