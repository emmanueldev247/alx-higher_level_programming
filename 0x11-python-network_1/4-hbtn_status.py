#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
response_body = response.text
print("Body response:")
print(f"\t- type: {type(response_body)}")
print(f"\t- content: {response_body}")
