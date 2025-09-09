#!/bin/bash

if [ "$#" -eq 0 ]; then
  echo "Error: No arguments provided."
  echo "Usage: $0 <molecule-args>"
  exit 1
fi

DOCKER_GID=$(getent group docker | cut -d: -f3)

docker run --rm -it \
  -v "$PWD":/src \
  -w /src \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --user "$(id -u)":"${DOCKER_GID}" \
  "local/infra-ansible-molecule:latest" \
  "$@"
