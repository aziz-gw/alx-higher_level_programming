#!/usr/bin/python3
"""
Takes  in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Perform the request
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")
