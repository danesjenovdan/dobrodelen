# ---------------------------------- WARNING ----------------------------------
# This file is primarily for production use with k8s
# See dev.Dockerfile for dev use with docker-compose
# ---------------------------------- WARNING ----------------------------------

FROM node:18-alpine as build

WORKDIR /nuxt_app

COPY package.json yarn.lock ./
RUN yarn

COPY . ./

RUN yarn build

FROM node:18-alpine

WORKDIR /app

COPY --from=build /nuxt_app/.output ./

EXPOSE 3000

CMD node server/index.mjs
