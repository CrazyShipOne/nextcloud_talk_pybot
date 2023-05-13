FROM python:3.11.2-slim

ENV LANG en_US.UTF-8 LC_ALL=en_US.UTF-8
COPY . /app

RUN cd /app \
    && python -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /var/cache/* \
    && rm -rf /tmp/* 


ENV PYTHONIOENCODING=utf-8

WORKDIR /app
ENTRYPOINT ["bash","start.sh"]