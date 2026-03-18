# Wireguard

this role takes care of installing and configuring wireguard:

- installs wireguard on the server
- generates the server config
- generates the client config (stored in local inventory)
- sets up ufw config (NAT) for wireguard (ufw rules have to configured in ufw role)

## Client config

configure clients in inventory `group_vars/wireguard` like so:

```yaml
wireguard_client_peers:
  - name: "alice"
    ip: "10.10.0.2/32"
```

configs are stored and encrypted (ansible-vault) locally in `inventories/production/wireguard_configs/clients`

to generate the QR code for the client config, run:

`ansible-vault view vpn-acme-all.conf.vault | qrencode -t ansiutf8`
