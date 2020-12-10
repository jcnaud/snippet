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

# Make release
rm -rf $ROOTDIR/jenkins_release/
mkdir -p $ROOTDIR/jenkins_release/${PROJECT_NAME}

cp -r $ROOTDIR/dist/* $ROOTDIR/jenkins_release/${PROJECT_NAME}/
cd $ROOTDIR/jenkins_release
tar -czf ${PROJECT_NAME}_${COMMIT}_${DATE}.tar.gz ${PROJECT_NAME}
