#!/bin/bash

docker pull morgannamie/python-almadencodingchallenge:latest

CURRENT_DIR=$(pwd)
docker run -v $CURRENT_DIR:/output/ morgannamie/python-almadencodingchallenge:latest
