#!/bin/bash

# Main kubectl alias
alias k='kubectl'

# Function to switch kubernetes namespace
kns() {
  if [ -z "$1" ]; then
    echo "Current namespace: $(kubectl config view --minify --output 'jsonpath={..namespace}')"
    echo "Usage: kns <namespace>"
    return 1
  fi
  
  kubectl config set-context --current --namespace="$1"
  echo "Switched to namespace: $1"
}

# Additional helpful kubectl aliases (optional - remove if not needed)
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deployments'
alias kgn='kubectl get nodes'
alias kdp='kubectl describe pod'
alias kl='kubectl logs'
alias kex='kubectl exec -it'

# Enable kubectl completion if available
if command -v kubectl &> /dev/null; then
  source <(kubectl completion bash)
  complete -F __start_kubectl k
fi
