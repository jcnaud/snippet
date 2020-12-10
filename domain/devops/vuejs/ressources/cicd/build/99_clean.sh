#!/bin/sh
set -e

# Source env file
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`
SCRIPTNAME=`basename $SCRIPT`
. $SCRIPTDIR/env.sh

#if [ ! "$(docker ps -q -f name=$DOCKER_NAME)" ]; then
#    if [ "$(docker ps -aq -f status=exited -f name=$DOCKER_NAME)" ]; then
#        # Clean docker
#        docker rm -f $DOCKER_NAME
#    fi
#    # Create docker
#    docker run \
#      -d \
#      --name $DOCKER_NAME \
#      -v "$SCRIPTDIR/../..":/home/node/app \
#      -w /home/node/app \
#      node:12-stretch \
#      sh -c 'while sleep 3600; do :; done'
#fi
echo "  Start 99_clean.sh"

echo -n "LOCAL_USER_ID=$(id -u)\nLOCAL_GROUP_ID=$(id -g)" > $SCRIPTDIR/docker-build/docker-compose.env;

if [ "$(docker ps -aq -f name=${DOCKER_NAME}_build_web)" ]; then
  echo "  Clean container docker build"
  docker-compose -f $SCRIPTDIR/docker-build/docker-compose.yml down
fi

if [ "$(docker ps -aq -f name=${DOCKER_NAME}_web)" ]; then
  echo "  Clean container docker prod"
  docker rm -f ${DOCKER_NAME}_web
fi

if [ "$(docker images -q -f reference=${DOCKER_NAME}_build_web)" ]; then
  echo "  Clean images docker build"
  docker rmi -f $(docker images -q -f reference=${DOCKER_NAME}_build_web | tail -n 1)
fi

if [ "$(docker images -q -f reference=${DOCKER_NAME}_web)" ]; then
  echo "  Clean images docker prod"
  docker rmi -f $(docker images -q -f reference=${DOCKER_NAME}_web | tail -n 1)
fi

echo "  End 99_clean.sh"