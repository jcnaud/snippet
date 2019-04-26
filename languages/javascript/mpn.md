# npm

Npm est un paquet écrit en javascript permetant l'installation de paquets.
nodejs est un compilateur/exécuteur javascript.


## Installation sous linux

source : https://lesbricodeurs.fr/articles/Comment-installer-npm-proprement/

npm est capable d'installer npm et nodejs.
sudo apt install curl



curl -sL https://deb.nodesource.com/setup_10.x > tt.sh
sudo bash ./tt.sh
rm tt.sh

sudo apt install nodejs



node -v
npm -v


edit http_server.js


const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});



source : https://lesbricodeurs.fr/articles/Comment-installer-npm-proprement/



mkdir ~/.npm-global
This command add ~/.npmrc file with specified option
npm config set prefix '~/.npm-global'

Add in .prolfile or in .bachrc
export PATH=~/.npm-global/bin:$PATH

sourcer ~/.profile


vue create my project



node http_server.js






node -v
npm -v

```bash
npm install npm@latest -g
```


For Debian and ubuntu:


curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs

npm install -g npm

Define where library will be installed in global mode (-g)

```bash
npm config set prefix '~/.npm-global'
echo "export PATH=~/.npm-global/bin:\$PATH" >> ~/.profile
source ~/.profile
```

Use npm without sudo
```bash
npm install -g typescript
```
ls ~/.npm-global/lib/node-modules



npm install -g @vue/cli
vue create my-project
