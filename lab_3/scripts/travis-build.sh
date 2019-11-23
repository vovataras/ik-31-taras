#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
PID_run=$!
pipenv run python monitoring.py &
PID_test=$!
sleep 120
kill $PID_test
kill $PID_run
exit 0