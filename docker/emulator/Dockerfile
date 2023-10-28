FROM node:18-alpine

RUN apk add openjdk11

RUN npm install -g firebase-tools
WORKDIR /srv/app

COPY ./docker/emulator/firebase.json .

CMD ["firebase", "emulators:start", "--project=flexier-app", "--import=./data", "--export-on-exit"]

