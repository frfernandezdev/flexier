FROM python:3.12-alpine

RUN mkdir -p /srv/app
WORKDIR /srv/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/server/entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
