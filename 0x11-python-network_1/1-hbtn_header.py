#!/usr/bin/python3

"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a request to the URL and retrieve the response
        with urllib.request.urlopen(url) as response:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in response.headers:
                print(response.headers['X-Request-Id'])
    except urllib.error.URLError as e:
        sys.exit(1)
