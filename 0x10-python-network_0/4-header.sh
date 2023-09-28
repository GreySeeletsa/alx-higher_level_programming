#!/bin/bash
# takes in URL as an arg, sends a GET request to it, and displays body of response
curl -s "$1" -H "X-School-User-Id: 98"
