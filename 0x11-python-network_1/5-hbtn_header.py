#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable"""

import requests
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]

    response = requests.get(my_url)

    print(response.headers["X-Request-Id"])
