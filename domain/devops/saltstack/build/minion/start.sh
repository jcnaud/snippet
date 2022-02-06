#!/bin/bash

# Variables from environement
: "${LOG_LEVEL:=info}"
: "${OPTIONS:=}"

# Start salt-minion
echo "INFO: Starting salt-minion with log level $LOG_LEVEL with hostname minion"
/usr/bin/salt-minion --log-level=$LOG_LEVEL $OPTIONS