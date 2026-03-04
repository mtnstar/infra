# k3s

- first node is setup as master and hostname has to be **k3s-1**

## argocd

- creates namespace argocd
- installs latest stable version of argocd
- sets up ingress and traefik servers transport; define `argocd_hostname` variable in inventory
