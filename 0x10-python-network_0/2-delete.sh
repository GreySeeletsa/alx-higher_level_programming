#!/bin/bash
# sends a DELETE request to URL passed as the first arg and displays body of response
curl -s "$1" -X DELETE
