# Saltstalk

## Context

Automate install management for many hosts(targeted hosts).

## Links

Tutorial: https://docs.saltproject.io/en/latest/topics/tutorials/walkthrough.html

## Overview

- One central server installed on the master host (Ex: your computer)
- Multiple client (Ex: one installed on each target host to manage)
All client and central master are connected with bi-directionnal bus communcation called "minions"

## Buld docker image

```bash
docker-compose build --build-arg SALT_VERSION=3003
```


## Run server


Links master conf full: https://docs.saltproject.io/en/latest/ref/configuration/examples.html#configuration-examples-master

## Usage

```bash
sudo ./INSTALL.sh
docker-compose up -d
```

Usage command

docker exec -it salt sh

```
# List keys
salt-key -L
 salt '*' cmd.run 'ls -l /etc'```


## Run the master manualy

```bash
# Run the master manualy in deman mode (background)
salt-master -d
# Or run master in foreground in debug mode
salt-master -l debug
```

Maste will use ports:
- 4505/TCP
- 4506/TCP


## Usage API

Test the API

### With token


```bash
# Get token

curl -sSk https://localhost:8000/login \
    -H 'Accept: application/x-yaml' \
    -d username=salt \
    -d password=mypassword \
    -d eauth=pam

# Use token
curl -sSk https://localhost:8000 \
    -H 'Accept: application/x-yaml' \
    -H 'X-Auth-Token: 697adbdc8fe971d09ae4c2a3add7248859c87079'\
    -d client=local \
    -d tgt='*' \
    -d fun=test.ping
```

### With cookie
With curl
```bash
# Write the cookie file:
curl -sSk https://localhost:8000/login \
      -c ~/cookies.txt \
      -H 'Accept: application/x-yaml' \
      -d username=saltdev \
      -d password=saltdev \
      -d eauth=auto

# Read the cookie file:
curl -sSk https://localhost:8000 \
      -b ~/cookies.txt \
      -H 'Accept: application/x-yaml' \
      -d client=local \
      -d tgt='*' \
      -d fun=test.ping
```
With python
```python
>>> import requests
>>> session = requests.Session()
>>> session.post('http://localhost:8000/login', json={
    'username': 'saltdev',
    'password': 'saltdev',
    'eauth': 'auto',
})
<Response [200]>
>>> resp = session.post('http://localhost:8000', json=[{
    'client': 'local',
    'tgt': '*',
    'fun': 'test.arg',
    'arg': ['foo', 'bar'],
    'kwarg': {'baz': 'Baz!'},
}])
>>> resp.json()
{u'return': [{
    ...snip...
}]}
```