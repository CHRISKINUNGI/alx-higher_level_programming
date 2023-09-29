#!/bin/bash
# sends a request to a URL and displays response body size
curl -s "$1" | wc -c
