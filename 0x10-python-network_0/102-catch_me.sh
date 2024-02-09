#!/bin/bash
# Bash script that makes a request to and causes the server to respond with a message containing You got me!, in the body of the response.
curl -sX POST http://0.0.0.0:5000/catch_me --data "You got me!"
