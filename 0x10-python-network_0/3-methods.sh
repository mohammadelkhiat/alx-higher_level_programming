#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | awk '/^Allow:/ {print substr($0, 8)}'
