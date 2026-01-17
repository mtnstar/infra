# Ansible Infrastructure Repository

🚀✨🙌💡🔥🌟🎉🥇👏

this is my ansible repo for managing infrastructure and deployments including:

- linux system config
- k3s cluster setup
- postgresql server
- all other deployments are managed with kustomize for deployment on k3s

directory structure:

- inventories: holds different environment inventories (e.g., production, staging)
- roles: contains reusable Ansible roles for various services and configurations
- playbooks: contains playbooks for deploying and managing services

## Getting Started

- start mtn-shell (see github.com/mtnstar/mtn-shell)
- clone this repository
- copy default inventory directory and customize it (e.g. ./inventories/default -> ./inventories/production)
- add desired public ssh keys to `inventories/production/ssh_keys/*.pub`

## Dynamic Role Tasks

for every role, the `tasks/main.yml` is symlinked from `roles/shared/tasks/dynamic_tasks_main.yml`. This enables us to split up role's tasks easely into seperate files which makes the code cleaner. It also makes it possible to only run a role's specific tasks by defining param tasks:

`ansible-playbook -i inventories/production/hosts playbooks/linux_bootstrap.yml -e '{task_list: ["2_user"]}'`

just add new task ymls in the format `1_mynewtask.yml` to `roles/$ROLE/tasks/` where as the leading number defines the order the task is being executed.

- see `roles/linux_base/tasks` for an example
- when creating a new role, symlink `roles/shared/tasks/dynamic_tasks_main.yml` to it's `tasks/main.yml`
- add main.yml path to `.prettierignore` since it hates symlinks ;) 

## Running molecule tests

inside mtn-shell in this repo run `molecule test -s linux_base`

as test container ghcr.io/mtnstar/infra-test-ubuntu:24.04 is used. (see https://github.com/mtnstar/infra-test-ubuntu)
