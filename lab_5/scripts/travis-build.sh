#!/bin/bash
set -ev
make run
make test-app
make push
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; docker push vovataras/lab4-examples:django-travis; else echo "PR skip deploy"; fi
exit 0