#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)"""

import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]

    response = requests.get(my_url)
    status = response.status_code

    if status >= 400:
        print(f'Error code: {status}')
    else:
        print(response.text)
