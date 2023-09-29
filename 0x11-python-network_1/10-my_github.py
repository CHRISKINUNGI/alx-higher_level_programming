#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(r.json().get('id'))
