#!/usr/bin/python3
"""Python script  that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)"""

import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]
    my_email = sys.argv[2]

    data = {'email': my_email}

    response = requests.post(my_url, data=data)
    print(response.text)
