# npm

Npm is a javascript package alow to install javascript package.
Node Js is a compiler/interpretor javascript.



## Install on linux

source : https://lesbricodeurs.fr/articles/Comment-installer-npm-proprement/

npm can install npm and Node JS.

### npm
```bash
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
sudo bash ./nodesource_setup.sh
rm nodesource_setup.sh
```

### Node Js
```bash
sudo apt update
sudo apt install nodejs
```

Check if the versions of nom and Node JS

```bash
node -v
npm -v
```

#### Option configuration de Node JS

For configure a launch of Node JS, you need to une a configuration file.


source : https://lesbricodeurs.fr/articles/Comment-installer-npm-proprement/

Create and edit le file
```bash
editor http_server.js
```

```javascript
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
```


### Make clean install

In order to make a clean install for a full acces for the userfor all project. We need to change the where all javascript packages are installed.

```bash
mkdir ~/.npm-global
```


This command add ~/.npmrc file with specified option
```bash
npm config set prefix '~/.npm-global'
```

Add in .prolfile or in .bachrc
```bash
export PATH=~/.npm-global/bin:$PATH
```


Restart the terminal or source the profile
```bash
source ~/.profile
```



## Run node

```bash
node http_server.js
```

### Update npm

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


vue create my project

npm install -g @vue/cli
vue create my-project
