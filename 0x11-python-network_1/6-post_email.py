#!/usr/bin/python3
"""
Takes  in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the
body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    data = {'email': email}
    # Perform the POST request
    response = requests.post(url, data=data)
    # Display the response body
    print(f"{response.text}")
