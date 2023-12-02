#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Perform the request
    response = requests.get(url)
    # Display the response body with tabulation
    print(
        f"Body response:\n"
        f"\t- type: {type(response.text)}\n"
        f"\t- content: {response.text}"
    )
