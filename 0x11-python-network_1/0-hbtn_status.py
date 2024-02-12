#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    response_body = response.read()

    print("Body response:")
    print(f"\t- type: {type(response_body)}")
    print(f"\t- content: {response_body}")
    print(f"\t- utf8 content: {response_body.decode('utf-8')}")
