#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    # Perform the request
    response = requests.get(url)
    # Display the value of X-Request-Id in the response header
    request_id = response.headers.get('X-Request-Id')
    print(f"{request_id}")
