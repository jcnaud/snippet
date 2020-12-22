# https://hub.docker.com/
FROM node:12-stretch

# Disable npm analytics questions when npn install
ENV NG_CLI_ANALYTICS false

# Create Working diretory
RUN mkdir -p /home/node/app && \
    chown node:node /home/node/app


# Script entrypoint
COPY entrypoint-dev /usr/local/bin/
RUN chmod a+x  /usr/local/bin/entrypoint-dev

# install vue cli
RUN npm install -g @vue/cli @vue/cli-service

#WORKDIR /home/node/app
#USER node:node

ENTRYPOINT ["/usr/local/bin/entrypoint-dev"]
