#!/bin/sh
set -e

# Source env file
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`
SCRIPTNAME=`basename $SCRIPT`
ROOTDIR="$SCRIPTDIR/../.."
COMMIT=`git rev-parse --short=8 HEAD`
DATE="`date '+%Y%m%dT%H%M'`"
. $SCRIPTDIR/env.sh

# Build docker
cd $ROOTDIR
docker build -t ${PROJECT_NAME}_web:${COMMIT} -f $ROOTDIR/cicd/build/docker-prod/web/Dockerfile .

# Tag to latest
docker tag  ${PROJECT_NAME}_web:${COMMIT} ${PROJECT_NAME}_web

# Remove previous docker if exist
files=`find $ROOTDIR/jenkins_release -type f -name "*.docker" -print`
if [ "${files}" ]; then
  rm $ROOTDIR/jenkins_release/*.docker
fi

# Save image
#docker save ${PROJECT_NAME}_web:${COMMIT} | gzip > $ROOTDIR/jenkins_release/${PROJECT_NAME}_web_${COMMIT}_${DATE}.docker
