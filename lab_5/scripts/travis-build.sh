#!/bin/bash
set -ev
make run-back
sleep 60*3
make test-app
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; fi
make push
exit 0