#!/usr/bin/python3
"""Python script that takes a URL sends a request to that URL
and displays the body of the response"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
