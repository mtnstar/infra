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

- inventories: holds different environment inventories (e.g., production, staging)
- roles: contains reusable Ansible roles for various services and configurations
- playbooks: contains playbooks for deploying and managing services

## Getting Started

- start mtn-shell (see github.com/mtnstar/mtn-shell)
- clone this repository
- customize inventory files in the `inventories` directory

## Running molecule tests

inside mtn-shell in this repo run `molecule -s linux_base`

as test container, https://github.com/mtnstar/infra-test-ubuntu is used
