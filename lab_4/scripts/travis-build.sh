#!/bin/bash
set -ev
docker build -t vovataras/lab4-examples:django-travis .
docker images
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; docker push vovataras/lab4-examples:django-travis; else echo "PR skip deploy"; fi
docker build -t vovataras/lab4-examples:monitoring-travis .
docker images
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; docker push vovataras/lab4-examples:monitoring-travis; else echo "PR skip deploy"; fi
exit 0