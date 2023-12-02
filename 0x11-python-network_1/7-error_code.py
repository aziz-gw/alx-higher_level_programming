#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Perform the GET request
        response = requests.get(url)
        # Raise HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        # Display the response body
        print(f"{response.text}")
        # Check for HTTP status code and print an error message if needed
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.response.status_code}")
