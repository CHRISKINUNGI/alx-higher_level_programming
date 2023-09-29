#!/bin/bash

# Send a GET request to the URL passed as an argument and display the status code

# Send the GET request and capture the output in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$response"

