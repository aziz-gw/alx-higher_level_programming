#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1]

try:
    # Perform the request
    response = requests.get(url)
    # Raise HTTPError for bad responses (4xx and 5xx)
    response.raise_for_status()
    # Display the value of X-Request-Id in the response header
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(f"{request_id}")

except requests.exceptions.HTTPError as e:
    # Handle HTTP errors
    print(f"Error code: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    # Handle other request-related errors
    print(f"Request error: {e}")
