FROM python:3.11-slim
ENV HOME=/home/tester
ARG USER_ID=1000

RUN mkdir -p /home/tester && chown ${USER_ID} /home/tester
RUN mkdir /src && chown ${USER_ID} /src
ENV PATH="$HOME/.local/bin:${PATH}"

USER ${USER_ID}
RUN cd /src

RUN pip install --upgrade pip \
  && pip install molecule ansible molecule-plugins[docker]

WORKDIR /src

ENTRYPOINT ["molecule"]
