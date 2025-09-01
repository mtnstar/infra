# disable version pinning for pip and apt intentionally
# kics-scan disable=965a08d7-ef86-4f14-8792-4a3b2098937e,02d9c71f-3ee8-4986-9c27-1a20d0d19bfc
FROM python:3.11-slim
ENV HOME=/home/tester
ARG USER_ID=1000

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
        lsb-release \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/tester \
  && chown ${USER_ID} /home/tester \
  && mkdir /src \
  && chown ${USER_ID} /src

ENV PATH="$HOME/.local/bin:${PATH}"

USER ${USER_ID}
WORKDIR /src

RUN pip install --no-cache-dir --upgrade pip==24.0 \
      molecule==25.7.0 \
      ansible==11.9.0 \
      molecule-plugins[docker]==25.8.12

HEALTHCHECK CMD molecule --version || exit 1

ENTRYPOINT ["molecule"]
