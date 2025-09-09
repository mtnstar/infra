# disable version pinning for pip and apt intentionally
# kics-scan disable=965a08d7-ef86-4f14-8792-4a3b2098937e,02d9c71f-3ee8-4986-9c27-1a20d0d19bfc
FROM ubuntu:24.04

# checkov:skip=CKV2_DOCKER_1 we're not using sudo here, just installing it
RUN apt-get update && \
      apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      gnupg \
      python3 python3-pip \
      lsb-release \
      sudo \
      && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash test-admin \
  && echo "test-admin ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

HEALTHCHECK CMD [ "ls", "/" ]

USER test-admin
