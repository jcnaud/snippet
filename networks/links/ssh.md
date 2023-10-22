# SSH


## Generate ssh key

```bash
# Generate RSA length 4096
ssh-keygen -t rsa -b 4096 -f id_rsa -C "your_conmment"
# Generate ed25519
ssh-keygen -t ed25519 -b 384 -f id_rsa -C "your_conmment"  
```

- **-t**: [ed25519,rsa1,rsa,dsa] # ed25519 est à privilégier. rsa1 correspond à la version 1 de ssh (à éviter utiliser), rsa et dsa correspondent à la version 2 (OK)
- **-b N**: # Key length 256, 384 or 521 bits for ed25519. For RSA, 2^n (4096 ou 8192). Don't use length under 2048 for RSA.
- **-f nom_fichier**: Fichier de sortie (par défaut id_ed25519, id_ed25519.pub, id_rsa, id-rsa.pub et id_sda,id_dsa.pub)
- **-C commentaire**: Commentary to help to identify the owner of the key et where it is. For example: you_name@your_computer.
```

## Afficher la fingerprint d'une clef publique

```bash
ssh-keygen -lf ~/.ssh/id_rsa.pub
ssh-keygen -l -E sha256 -f ~/.ssh/id_rsa.pub
ssh-keygen -l -E sha1 -f ~/.ssh/id_rsa.pub
ssh-keygen -l -E md5 -f ~/.ssh/id_rsa.pub
```

Générer un mot de passe sécure (aléatoire) de 6 caractères
```bash
pwgen -s
```
ou de 16 caractères
```bash
pwgen -s 16
```

| Description | commandes|
|-- |-- |
| Connection ssh en ignorant les erreurs du au knows_host (IP differente) | ```ssh -o StrictHostKeyChecking=no username@hostname.com``` |
| Lancer une commande avec ssh | ```ssh alkante@www.alkante.com 'ls -al'``` |
| Lancer une commande avec ssh et avec intéraction | ```ssh -t alkante@www.alkante.com 'top'``` |
| Changer le passphrase de la clef | ```ssh-keygen -p -f id_rsa``` |



## Autoriser une clef utilisateur
```bash
mkdir -p ~/.ssh  
chmod go-rwx ~/.ssh  
touch ~/.ssh/authorized_keys  
chmod go-rwx ~/.ssh/authorized_keys  
echo "publickeys_______" > ~/.shh/authorized_keys  

ssh-keygen -t ed25519 -b 384 -C nagios@shamrock  
ssh-keygen -t ed25519 -N "" -b 384 -f /root/.ssh/id_ed25519 -C  root@VMECHANGE  
```

## copie vers le serveur d'id_ed25519.pub
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub nagios@linux4.alkante.com
```

## sur le serveur
```bash
chmod go-w ~/
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

/usr/bin/ssh-keygen -t ed25519 -N "" -f ${HOME}/.ssh/temporary_id_ed25519
/usr/bin/ssh-copy-id -i ${HOME}/.ssh/temporary_id_ed25519 root@${TARGET_SERVER}

#convert ppk to openssh
puttygen ccvol.ppk -O private-openssh -o ccvol
#convert openssh to putty
puttygen id_ed25519 -O private -o id_ed25519.ppk
puttygen id_rsa -o id_rsa.ppk
#convert putty public to openssh public
ssh-keygen -i -f ssh2.pub > openssh.pub
```

### générer des paires de clés pour un user ###
```bash
user="egoudard"
ssh-keygen -t ed25519 -N "" -b 384 -f ${user} -C "${user}@${user}.alkante.al"
puttygen "${user}" -o "${user}.ppk"
puttygen -L "${user}.ppk" > "${user}.ppk.pub"
tar -czvf "sshkeys_${user}.tgz" ${user}*
rm ${user}*

#ssh fingerprint
ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub

#test ssh
test_ssh()
{
cmdlog "ssh ${SSH_OPT} ${SRV_DST} \"echo -n > /dev/null 2>&1\""
}

#envoyer un bash à executer sur plein de serveurs
ssh root@linux28.alkante.hbgt 'bash -s' < get_dom0_usage.sh
for i in alk0008 linux26 linux27 linux12old linux6; do echo $i; ssh root@${i}.alkante.hbgt 'bash -s' < get_dom0_usage.sh;done

#tunnel SSH (port 9101 du srv distant redirigé vers 19101 local via un tunnel ssh)
ssh -N -f alkante@linux17.alkante.com -L19101:linux17.alkante.com:9101 sleep 60
#tunnel SSH (port 127.0.0.1:8080 du srv distant(81.255.120.68) redirigé vers 19101 local via un tunnel ssh)
ssh -N -f alkante@81.255.120.68 -L19101:127.0.0.1:8080

#mode full non-interactive (ignore errors & fingerprints changes, etc...)
SSH_OPT="-o BatchMode=yes -o PasswordAuthentication=no -o StrictHostKeyChecking=no -o CheckHostIP=no -o ConnectTimeout=30 -i ${SSH_KEY}"

#après les MAJ ubuntu 16.04, ajoutez dans votre config client ssh:
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> .ssh/config

```


## Tunnel

Le Tunnel SSH permet de faire passé un flux réseau de n'importe quel nature.

```bash
ssh -L 1234:localhost:22 remotehost
```

```ascii
+--------------+   +--------------+
|     You      |   |  remotehost  |
|              |   | +----------+ |
|              |   | |localhost | |
|         1234 O===O->22        | |
|              |   | +----------+ |
+--------------+   +--------------+
```

```bash
ssh -L 1234:endhost:22 remotehost
```
```ascii
+--------------+   +--------------+   +--------------+
|     You      |   |  remotehost  |   |   endhost    |
|              |   |              |   |              |
|              |   |              |   |              |
|         1234 O==================O--->22            |
|              |   |              |   |              |
+--------------+   +--------------+   +--------------+
```

```bash
ssh -R 1234:localhost:22 remotehost
```
```ascii
+--------------+   +--------------+
|    You       |   |  remotehost  |
| +----------+ |   |              |
| |localhost | |   |              |
| |       22 <-O===O 1234         |
| +----------+ |   |              |
+--------------+   +--------------+
```

```bash
ssh -R 1234:endhost:22 remotehost
```
```ascii
+--------------+   +--------------+   +--------------+
|     endhost  |   |  You         |   |  remotehost  |
|              |   |              |   |              |
|              |   |              |   |              |
|         22   <---O==================O 1234         |
|              |   |              |   |              |
+--------------+   +--------------+   +--------------+
```

Pour des raisons de sécurité, utilisé cette commande avec un autre compte si l'acces est public.
