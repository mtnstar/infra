# Linux Bootstrap

the goal of this role is to setup linux system after it has been bootstrapped with a minimal installation based on ubuntu 24.04 minimal cloud init image.

to run this role/playbook against a freshly bootstraped host, use the following command:

`ansible-playbook -i inventories/production/hosts playbooks/linux_bootstrap.yml --limit=my-new-host -e ansible_user=default-bootstrap -e ansible_port=22`
