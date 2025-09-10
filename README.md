# Ansible Infrastructure Repository

🚀✨🙌💡🔥🌟🎉🥇👏

this is my ansible repo for managing infrastructure and deployments including:

- linux system config
- nextcloud
- mailpit
- vaultwarden
- p2p stack: deluge, radarr, sonarr, ...
- plex server

directory structure:

* inventories: holds different environment inventories (e.g., production, staging)
* roles: contains reusable Ansible roles for various services and configurations
* playbooks: contains playbooks for deploying and managing services

## Getting Started

- clone this repository
- `./bin/init.sh` to set up local environment
- customize inventory files in the `inventories` directory

## Running molecule tests

`./bin/molecule.sh -s linux_base`
