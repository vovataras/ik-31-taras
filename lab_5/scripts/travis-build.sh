#!/bin/bash
set -ev
make run-back
make test-app-back
sleep 120
make push
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; fi
exit 0