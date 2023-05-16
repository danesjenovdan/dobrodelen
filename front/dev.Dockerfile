# ---------------------------------- WARNING ----------------------------------
# This file is primarily for development use with docker-compose
# See k8s.Dockerfile for production and k8s use
# ---------------------------------- WARNING ----------------------------------

FROM node:18-alpine

WORKDIR /nuxt_app

COPY package.json yarn.lock ./
RUN yarn

EXPOSE 3000

CMD yarn dev
