#!/bin/bash
# This sript will use **init** directory and generate **data** and **var** directories.

# Stop the script if one error occur
set -e

# Computed variables
SCRIPT=`readlink -f $0`
SCRIPTDIR=`dirname $SCRIPT`

dir_src=$SCRIPTDIR/init/salt/master.d
dir_dest=$SCRIPTDIR/data/salt/master.d
if [ ! -d "$dir_dest" ]; then
  mkdir -p $dir_dest
  chmod 755 $dir_dest

  cp $dir_src/* $dir_dest/
  chmod -R 755 $dir_dest
fi

dir_dest=$SCRIPTDIR/data/salt/pki_master
if [ ! -d "$dir_dest" ]; then
  mkdir -p $dir_dest
  chmod 755 $dir_dest
  chown 450:450 $dir_dest
fi

dir_src=$SCRIPTDIR/init/salt/minion.d
dir_dest=$SCRIPTDIR/data/salt/minion.d
if [ ! -d "$dir_dest" ]; then
  mkdir -p $dir_dest
  chmod 755 $dir_dest

  cp $dir_src/* $dir_dest/
  chmod -R 755 $dir_dest
fi


dir_src=$SCRIPTDIR/init/minion/config
dir_dest=$SCRIPTDIR/data/minion/config
if [ ! -d "$dir_dest" ]; then
  mkdir -p $dir_dest
  chmod 755 $dir_dest

  cp $dir_src/* $dir_dest/
  chmod -R 755 $dir_dest
fi



