#!/bin/sh

# Check if a URL is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <bit.ly URL>"
    exit 1
fi

# Fetch headers and check for Location
location=$(curl -s -I "$1" | grep -i 'Location:' | cut -d' ' -f2-)

# Check if we found a location and print it
if [ -n "$location" ] && [ "$location" != "$1" ]; then
    echo "$location"
else
    echo "No redirection found or invalid URL"
    exit 1
fi
