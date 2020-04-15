#!/bin/bash

# Test with
#    ./test_arguments.sh 1 2 3

echo '$0' $0
echo '$1' $1
echo '$2' $2
echo '$2' $3
echo '$#' $#  # Number off argument
echo '$@' $@  # All arguments array like
echo '$*' $*  # All arguments IFS (internal field separator), i.e. default space separed
echo '$?' $?  # Return code


echo '$-' $-  # current options set
echo '$$' $$  # PID
echo '$_' $_  # most recent parameter (or the abs path of the command to start the current shell immediately after startup).
echo '$IFS' $IFS # is the (input) field separator.
echo '$?' $? # is the most recent foreground pipeline exit status.
echo '$!' $! # is the PID of the most recent background command.

for i in $@;
do
    echo "The $i"
done

for i in $*
do
    echo "The $i"
done

