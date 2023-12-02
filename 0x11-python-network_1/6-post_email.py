#!/usr/bin/python3
"""
Takes  in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the
body of the response.
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data for the POST request
data = {'email': email}

try:
    # Perform the POST request
    response = requests.post(url, data=data)
    # Raise HTTPError for bad responses (4xx and 5xx)
    response.raise_for_status()
    # Display the response body
    print(f"{response.text}")

except requests.exceptions.HTTPError as e:
    # Handle HTTP errors
    print(f"Error code: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    # Handle other request-related errors
    print(f"Request error: {e}")
