#!/usr/bin/python3
"""Python scirpt that takes a URL and email, sends a POST request
with email as parameter and displays the body of the response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
