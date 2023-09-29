#!/usr/bin/python3
"""Python script that sends a request to a URL and displays the
value of the X-Request-Id variable found in the response header"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    r_id = response.headers['X-Request-Id']
    print(r_id)
