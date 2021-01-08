#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

IMAGE="promobot_edu"
PARAMS="--network=host"

docker build  $PARAMS -t "$IMAGE" .
