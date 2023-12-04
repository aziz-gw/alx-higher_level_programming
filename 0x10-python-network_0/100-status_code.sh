#!/bin/bash
#sends a request to a URL passed as an arg;displays status code of the response
curl -sI "$1" -o /dev/null -w '%{http_code}\n'
