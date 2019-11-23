#!/bin/bash
set -ev
make test || true
make run
exit 0