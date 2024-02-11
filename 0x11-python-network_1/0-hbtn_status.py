#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    response_body = response.read()

    print("Body response:")
    print("    - type: <class 'bytes'>")
    print(f"    - content: {response_body}")
    print("    - utf8 content: OK")
