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
docker-compose build salt --build-arg SALT_VERSION=3003
docker-compose build minion
```

Run
```bash
docker-compose up
```

Accept the ssh key from the minion
```
# Display minion id
docker exec minion cat /etc/salt/minion_id
# Display key on master
docker exec -it salt salt-key -L
# Accept the key
docker exec -it salt salt-key -a 7c9c7d373ca0
```




## Troubleshooting

The Salt Master server's public key did not authenticate!

```
# On minion
docker exec minion rm /etc/salt/pki/minion/minion_master.pub
# Retart
```

## Usage

Connect ```docker exec -it salt sh```
| Command | Description |
|- |- |
| ```salt '*' test.ping``` | Ping all |
| ```salt-run '*' sys.doc``` | Display all salt command |
| ```salt-run '*' disk.usage``` | Display all salt command |
| ```salt '*' cmd.run 'ls -l /etc'``` | Run command on all salt command |
| ```salt '*' pkg.install vim``` | install vim |
| ```salt '*' state.apply vim``` | check install vim |


```sh
mkdir -p /srv/salt
cat <<EOF > /srv/salt/vim.sls
vim-enhanced:
  pkg:
    - installed
EOF
```
mkdir -p /srv/salt
cat <<EOF > /srv/salt/tree.sls
tree:
  pkg:
    - installed
EOF
salt '*' state.apply tree
```

```
# Run sls
salt '*' state.apply vim
```




echo 


/srv/salt/vim.sls



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