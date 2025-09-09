#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]:-$_}")")"

ansible-galaxy collection install -r requirements.yml

docker build -f "$SCRIPT_DIR"/Molecule.dockerfile \
  --build-arg USER_ID="$(id -u)" \
  -t "local/infra-ansible-molecule" "$SCRIPT_DIR"
