# Linux Base Role

## ufw

define firewall default rules or rules for host groups and specific hosts.

see `roles/linux_base/defaults/main.yml` for defined default rules and config.

override them in your inventory:

1. in group_vars

e.g. inventories/production/group_vars/linux_routers/vars.yml
```yaml
...
ufw_group_rules:
  - rule: allow
    port: "443"
    proto: tcp
    interface: "lanbr0"
    direction: in
    from_ip: "{{ secure_lan_cidr }}"
    comment: "HTTPS secure LAN"
  - rule: allow
    port: "53"
    proto: udp
    interface: "eth1"
    direction: in
    from_ip: "{{ guest_lan_cidr }}"
    comment: "DNS guest LAN"
...
```

2. in host_vars

e.g. inventories/production/host_vars/myhost/vars.yml
```yaml
...
ufw_host_rules:
  - rule: allow
    port: "80"
    proto: tcp
    interface: "eth1"
    direction: in
    from_ip: "192.168.42.2"
    comment: "HTTP secure LAN"
...
```

3. in all hosts vars for defaults

e.g. inventories/production/group_vars/all/vars.yml
```yaml
ufw_default_rules:
  - rule: allow
    port: "42"
    proto: tcp
    comment: "Special service access"
...
```

this overrides rules defined in this roles defaults
