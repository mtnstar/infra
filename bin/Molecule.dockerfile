FROM python:3.11-slim
ENV HOME=/home/tester
ARG USER_ID=1000

RUN mkdir -p /home/tester \
  && chown ${USER_ID} /home/tester \
  && mkdir /src \
  && chown ${USER_ID} /src

ENV PATH="$HOME/.local/bin:${PATH}"

USER ${USER_ID}
WORKDIR /src

RUN pip install --no-cache-dir molecule==25.7.0 \
      ansible==11.9.0 \
      molecule-plugins[docker]==25.8.12

HEALTHCHECK CMD molecule --version || exit 1

ENTRYPOINT ["molecule"]
