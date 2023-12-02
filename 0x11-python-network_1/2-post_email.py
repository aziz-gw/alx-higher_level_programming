#!/usr/bin/python3

"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) < 3:
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Perform the POST request
with urllib.request.urlopen(url, data) as response:
    # Read and decode the response body
    response_body = response.read().decode('utf-8')
    print(response_body)
