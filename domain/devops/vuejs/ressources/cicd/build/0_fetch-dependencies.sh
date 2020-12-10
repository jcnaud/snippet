#!/bin/sh
set -e

# Source env file
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`
SCRIPTNAME=`basename $SCRIPT`
. $SCRIPTDIR/env.sh


## Prompt nexus.alkante.com password if needed
#if [ -z "${NEXUS_USR}" ]; then
#  echo -n "Enter nexus.alkante.com login: "
#  read NEXUS_USR
#fi
#if [ -z "${NEXUS_PSW}" ]; then
#  echo -n "password: " 
#  stty -echo
#  IFS= read -r NEXUS_PSW
#  stty echo
#  printf '\n'
#fi

#[ -z "${NEXUS_EMAIL}" ] && NEXUS_EMAIL='jenkins@alkante.com'
#[ -z "${REPO_COMPOSER_DOMAIN}" ] && REPO_COMPOSER_DOMAIN='nexus.alkante.com'
#[ -z "${REPO_NPM}" ] && REPO_NPM='nexus.alkante.com/repository/npm'


echo -n "LOCAL_USER_ID=$(id -u)\nLOCAL_GROUP_ID=$(id -g)" > $SCRIPTDIR/docker-build/docker-compose.env;

# Create dockers
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml build
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml up -d

sleep 2 # Wait entrypoint run

# Exec
docker exec --user node:node -w /home/node/app ${DOCKER_NAME}_build_web /bin/bash -c " \
  set -e; \
  npm install;"

## Exec
#docker exec --user node:node -w /home/node/app ${DOCKER_NAME}_web /bin/bash -c ' \
#  set -e; \
#  export TOKEN=$(curl -s \
#  -H "Accept: application/json" \
#  -H "Content-Type:application/json" \
#  -X PUT \
#  -d '"'"'{"name":"'$NEXUS_USR'","password": "'$NEXUS_PSW'"}'"'"' \
#  https://'$REPO_NPM'/-/user/org.couchdb.user:'$NEXUS_USR' 2>&1 | grep -Po \
#  '"'"'(?<="token":")[^"]*'"'"'); \
#  echo Add repo : '$REPO_NPM'; \
#  npm set @alkante:registry "https://'$REPO_NPM'/"; \
#  npm set //'$REPO_NPM'/:_authToken=$TOKEN; \
#  sleep 1; \
#  npm install;'


# Stop dockers
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml down
