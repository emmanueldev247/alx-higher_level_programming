#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else ""
    passwd = sys.argv[2] if len(sys.argv) > 2 else ""

    url = f"https://api.github.com/users/{user}"

    my_token = f"Bearer {passwd}"
    data = {"Authorisation": my_token}

    response = requests.get(url, data=data).json()
    print(response.get('id'))
