#!/bin/sh
set -e

# Source env file
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`
SCRIPTNAME=`basename $SCRIPT`
. $SCRIPTDIR/env.sh

echo -n "LOCAL_USER_ID=$(id -u)\nLOCAL_GROUP_ID=$(id -g)" > $SCRIPTDIR/docker-build/docker-compose.env;

# Create dockers
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml build
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml up -d

sleep 2 # Wait entrypoint run

# Exec
docker exec --user node:node -w /home/node/app ${DOCKER_NAME}_build_web /bin/bash -c " \
  set -e; \
  npm run lint;"

# Stop dockers
docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml down
