#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)"""

import sys
from urllib import request
from urllib import parse
from urllib import error


if __name__ == "__main__":
    my_url = sys.argv[1]

    try:
        with request.urlopen(my_url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)

    except error.HTTPError as e:
        print(f"Error code: {e.code}")
