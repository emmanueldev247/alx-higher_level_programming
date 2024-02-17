#!/usr/bin/python3
"""Python script that takes a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter"""

import sys
import requests


if __name__ == "__main__":
    my_url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    params = {"q": letter}

    try:
        response = requests.post(my_url, data=params).json()
        if len(response) == 0:
            print("No result")
        else:
            print(f"[{response['id']} {response['name']}")
    except Exception:
        print("Not a valid JSON")
