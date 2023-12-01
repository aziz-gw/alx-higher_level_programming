#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
url="$1"; response=$(curl -L -s -w "\n%{http_code}\n" "$url"); echo "$response";body=$(echo "$response" | awk 'END{if($2 == 200) print $0}'); echo "$body"
