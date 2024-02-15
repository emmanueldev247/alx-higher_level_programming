#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable"""

import urllib.request
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]
    with urllib.request.urlopen(my_url) as response:
        response_body = response.read()

        headers = response.headers
        header_val = headers.get("X-Request-Id")
        print(header_val)
