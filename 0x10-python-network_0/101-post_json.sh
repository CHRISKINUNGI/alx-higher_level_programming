#!/bin/bash
# Send a POST request with the JSON data from the file and display the response body
jq empty "$2" && curl -s -H "Content-Type: application/json" -X POST --data @"$2" "$1"

