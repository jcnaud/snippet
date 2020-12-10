# README
<!-- TOC -->

- [README](#readme)
  - [Overview](#overview)
  - [Start developpement](#start-developpement)
    - [Change mode dev, prod](#change-mode-dev-prod)
    - [Run unit test](#run-unit-test)
  - [Stop developpement](#stop-developpement)
  - [General Docker commands](#general-docker-commands)
  - [Advanced Docker commands](#advanced-docker-commands)
    - [Clean commands](#clean-commands)
    - [Monitoring commands](#monitoring-commands)

<!-- /TOC -->

## Overview

This file give commands to start development with docker.

Require:
 - Docker installed.
 - Docker well configured, cf. **/etc/docker/deamon.json**
 - User in docker group to avoid sudo/su right

## Start developpement

Make these commands in this directory ```cd ./cicd/dev```.

Run container
```bash
# Put UID and GID in env file
echo -e "LOCAL_USER_ID=$(id -u)\nLOCAL_GROUP_ID=$(id -g)" > docker-compose.env;

# Build dev image
docker-compose build

# Run containers
docker-compose up
```


In an other terminal, connect as www-data to the dev container
```bash
# Connect to container  as node
docker exec --user node -w /home/node/app -it vuejs_devops_dev_web bash
```

In container
```bash
# Install
npm install

# Serve
npm run dev 
```

The url web site are http://localhost:8080


Option, if you what to add vue-cli comand line

```bash
docker exec --user root -w /home/node/app -it vuejs_devops_dev_web npm i -g @vue/cli
```

Inpect webpack config : ```vue inspect --mode production > output.prod.js```

### Change mode dev, prod
Edit the ```./site/.env```

```bash
# mode dev
APP_ENV=dev
# mode prod
APP_ENV=prod
```

### Run unit test

```bash
# Run unit test
php bin/phpunit
```

## Stop developpement

Make these commands in this directory ```cd ./cicd/dev```.

```bash
# Shutdown containers
docker-compose down

# Remove dev image
docker rmi template-vue-python-backend_dev_web
docker rmi template-vue-python-backend_dev_db
```

## General Docker commands

| Description | Commandes |
|- |- |
| Display images            | ```docker images``` |
| Remove image              | ```docker rmi myimages``` |
|- |- |
| Display all running containers | ```docker ps``` |
| Display all containers    | ```docker ps -a``` |
| Remove container          | ```docker rm mycontainer``` |
| Display info container    | ```docker inpect mycontainer``` |
| Display container ouput   | ```docker logs mycontainer``` |
| Stop container            | ```docker stop mycontainer``` |
| Kill container            | ```docker kill mycontainer``` |
|- |- |
| Connection as root | ```docker exec --user 0 -w / -it template-vue-python-backend_dev_web bash``` |
| Connection as www-data | ```docker exec --user www-data -w /var/www/html -it template-vue-python-backend_dev_web bash``` |
| Connection as postgres | ```docker exec --user postgres -it template-vue-python-backend_dev_db bash``` |
| Run composer install | ```docker exec --user www-data -w /var/www/html -it template-vue-python-backend_dev_web composer install ``` |

## Advanced Docker commands


### Clean commands
```bash
# Stop all container
docker stop $(docker ps -a -q)

# Remove all container
docker rm $(docker ps -a -q)

# Delete all image with name or tag as "<none>"
docker rmi `docker images| egrep "<none>" |awk '{print $3}'`
```

### Monitoring commands

```bash
# Watch all container
watch -n 1 "docker ps -a"

# Watch all images
watch -n 1 "docker images"

# Watch all resources container
docker stats
```
