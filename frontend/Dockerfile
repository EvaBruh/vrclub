FROM node:18.16
WORKDIR /frontend

COPY vite.config.js .
COPY index.html .
COPY ./src /frontend/src
COPY package*.json /frontend/

RUN npm install
RUN npm run build

COPY . .