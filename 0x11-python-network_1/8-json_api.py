#!/usr/bin/python3
"""Python script that takes a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter"""

import sys
import requests


if __name__ == "__main__":
    my_url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    params = {"q": letter}

    response = requests.post(my_url, data=params)

    try:
        response = response.json()
        if len(response) == 0:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except Exception:
        print("Not a valid JSON")
