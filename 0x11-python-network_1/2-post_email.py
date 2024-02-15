#!/usr/bin/python3
"""Python script  that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)"""

import sys
from urllib import request
from urllib import parse


if __name__ == "__main__":
    my_url = sys.argv[1]
    my_email = sys.argv[2]

    data = parse.urlencode({'email': my_email}).encode('utf-8')

    req = request.Request(my_url, data=data, method="POST")
    with request.urlopen(req) as response:
        response_body = response.read()

        print(response_body.decode('utf-8'))
