#!/bin/bash
# takes in a URL, sends request to it, and displays size of the body of response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
