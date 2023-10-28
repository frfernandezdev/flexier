FROM python:3

ARG SECRET_PASSPHRASE
ARG FIREBASE_SDK_ADMIN


RUN mkdir -p /srv/app
WORKDIR /srv/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ .

CMD gunicorn --bind 0.0.0.0:$PORT 'wsgi:create_wsgi()'
