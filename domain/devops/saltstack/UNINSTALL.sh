#!/bin/bash
# This sript will delete **data** directory.

# Stop the script if one error occur
set -e

# Computed variables
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`

if [ -d "$SCRIPTDIR/data" ]; then
    rm -rf ${SCRIPTDIR}/data
fi
