#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

# Display the value of X-Request-Id in the response header
request_id = response.headers.get('X-Request-Id')
print(f"{request_id}")
