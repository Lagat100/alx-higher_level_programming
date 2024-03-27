#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me  response "You got me!
curl -s -X POST -H "Referer: You got me!" 0.0.0.0:5000/catch_me
