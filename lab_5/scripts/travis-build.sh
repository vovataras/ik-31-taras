#!/bin/bash
set -ev
make run &
PID_run=$!
make test-app &
PID_test=$!
sleep 120
kill $PID_test
kill $PID_run
make push
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; fi
exit 0