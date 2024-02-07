#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -sX POST -d @$2  $1
