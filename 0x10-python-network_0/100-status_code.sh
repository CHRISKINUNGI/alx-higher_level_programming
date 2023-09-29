#!/bin/bash

# Send a GET request to the URL passed as an argument and display the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
