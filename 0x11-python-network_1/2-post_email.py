#!/usr/bin/python3
"""Python Script that takes a URL and an email, sends a POst
request with the email as a parameter, and displays the response body
(decoded in utf-8)"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
        request = urllib.request.Request(sys.argv[1], data)
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except Exception as e:
        print(e)
