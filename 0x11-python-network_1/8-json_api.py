#!/usr/bin/python3

"""
Takes in letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    # URL for the POST request
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    # Prepare the data for the POST request
    data = {'q': q}

    try:
        # Perform the POST request
        response = requests.post(url, data=data)
        # Raise HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        # Try to parse the response as JSON
        json_data = response.json()

        # Check if the JSON is properly formatted and not empty
        if json_data and isinstance(json_data, dict):
            # Display the id and name
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            # Display No result if the JSON is empty
            print("No result")
    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
