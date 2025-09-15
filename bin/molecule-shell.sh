#!/bin/bash
DOCKER_GID=$(getent group docker | cut -d: -f3)

docker run --rm -it \
  -v "$PWD":/src \
  -w /src \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --user "$(id -u)":"${DOCKER_GID}" \
  --entrypoint /bin/bash \
  "local/infra-ansible-molecule:latest" \
