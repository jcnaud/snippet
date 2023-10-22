# NRPE


## Context

The nrpe protocol allow Nagios server (with pluging check_nrpe) to get monitoring info on service nrpe.
Service NRPE run script and return reponse with criticity level (warnionf, critical, ...) 

```
    Host nagios                 Host to monitor
+-----------------------+     +---------------+
|                       |     |               |
|  Nagios -> check_nrpe ------> service nrpe  |
|                       |     |               |
+-----------------------+     +---------------+
```

## Links




## Install

### On nagios Hoest

```bash replay
# Installcheck_nrpe for nagios
apt-get install install nagios-nrpe-plugin
```

Add NRPE template command in **/usr/local/nagios/etc/commands.cfg**

```bash no-replay
cat <<EOF >> /etc/nagios/nrpe.cfg

######
# NRPE
######

# 'check_nrpe' command definition
define command{
command_name check_nrpe
command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}
EOF
```

### On host to monitor

```bash
# Install NRPE service 
apt-get install nagios-nrpe-server
apt-get install nagios-plugins

# Change the service listening ip: Change the io 1.2.3.4 by your public ip
sed -r 's/^([\t ]*#[\t ]*)(allowed_hosts=)(.*)$/\2127.0.0.1, 1.2.3.4/gm' /etc/nagios/nrpe.cfg
```

(option) install community script

You can install many community script for NRPE:
-  https://github.com/skyscrapers/monitoring-plugins.git


```bash
# Copy community script in cd /usr/lib/nagios/plugins/

# Fix owner
chown -R root: /usr/lib/nagios/plugins/your_script
# Fix rights
chmod 0755 /usr/lib/nagios/plugins/your_script
```

Add command in NRPE service

```bash
cat <<EOF >> /etc/nagios/nrpe.cfg

# Peronnal Commandes
# Check space disk
command[check_disk]=/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /
# Check CPU load
command[check_load]=/usr/lib/nagios/plugins/check_load -r
# Check RAM
command[check_memory]=/usr/lib/nagios/plugins/monitoring-plugins/check_memory -w 20 -c 5
# Check no disk mount as read only
command[check_ro_mounts]=/usr/lib/nagios/plugins/monitoring-plugins/check_ro_mounts -X tmpfs
EOF
```



```bash
# Restart the service
sevice nagios-nrpe-server reload
```


Tester les commandes nrpe coté remote (Ex: test de check_disk)
```bash test 
# On the nagios host, you can manualy call the NRPE service
/usr/lib/nagios/plugins/check_nrpe -H 1.2.3.4 -c check_disk
```


## Example of bash NRPE script

Create script name "openfile.sh"

```bash
#!/bin/bash
OK=0
WARNING=1
CRITICAL=2
UNKNOWN=3
WARNING_THESHOLD=2000
CRITICAL_THESHOLD=5000

openfiles=`cat /proc/sys/fs/file-nr | awk '{print $1}'`

if [ $openfiles -lt $WARNING_THESHOLD ]; then
  echo “OK. There are $openfiles Openfiles” exit $OK   
elif [ $openfiles -lt $CRITICAL_THESHOLD ]; then
  echo “WARNING. There are $openfiles Openfiles” exit $WARNING
elif [ $openfiles -ge $CRITICAL_THESHOLD ]; then
  echo “CRITICAL. There are $openfiles Openfiles” exit $CRITICAL
else
   echo “UNKNOWN. Not able to calculate the number of openfiles” exit $UNKNOWN
fi
```

```bash
# make the script executable
chmod +x openfile.sh

# Test it
./openfile.sh
# Check the return code
echo $?
```

Add command in the service NRPE config
```
command[check_openfiles]=/user/local/nagios/libexec/openfiles.sh
```

## Example of python NRPE script

```python
#!/usr/bin/python
import os
import sys

OK=0
WARNING=1
CRITICAL=2
UNKNOWN=3
WARNING_THESHOLD=2000
CRITICAL_THESHOLD=5000

with open('/proc/sys/fs/file-nr') as _file:
    first_line = _file.readline()

openfiles = int(first_line.split('\t')[0])

if openfiles < WARNING_THESHOLD:
  print('OK. There are {} Openfiles exit {}'.format(openfiles, OK))
  sys.exit(OK)
elif openfiles < CRITICAL_THESHOLD:
  print('WARNING. There are {} Openfiles exit {}'.format(openfiles, WARNING))
  sys.exit(WARNING)
elif openfiles >= CRITICAL_THESHOLD:
  print('CRITICAL. There are {} Openfiles exit {}'.format(openfiles, CRITICAL))
  sys.exit(CRITICAL)
else:
  print('UNKNOWN. Not able to calculate the number of openfiles” exit {}'.format(openfiles, UNKNOWN))
  sys.exit(UNKNOWN)

```

```bash
# Test it
python ./openfile.sh
# Check the return code
echo $?
```