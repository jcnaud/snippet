# Vue JS with DevOps

## Requirements

TODO: Install docker and docker-compose


## Init
```bash
export PROJECT_NAME="test3"

mkdir -p $PROJECT_NAME
cp -r ./ressources/cicd ./$PROJECT_NAME/cicd

#Option, change project name
find ./$PROJECT_NAME/cicd -type f -exec sed -i 's/vuejs_devops/'$PROJECT_NAME'/g' {} \;

cd $PROJECT_NAME/cicd/dev

# Put UID and GID in env file
echo -e "LOCAL_USER_ID=$(id -u)\nLOCAL_GROUP_ID=$(id -g)" > docker-compose.env;

# Build dev image
docker-compose build

# Run containers
docker-compose up -d
```


In an other terminal, connect as www-data to the dev container
```bash
# Connect to container  as node
docker exec --user node -w /home/node/app -it $PROJECT_NAME'_dev_web' bash
```

```bash
export PROJECT_NAME="test3"
vue create $PROJECT_NAME
# Project name: $PROJECT_NAME
# Othrer : Y
mv $PROJECT_NAME/* .
mv $PROJECT_NAME/.* .
rmdir $PROJECT_NAME

npm install

exit
```

Go to ```./cicd/dev/README.md``` of your project to start the developpement

## Developpement trick

Inpect vue+webpack configuration: ```vue inspect```

Display plugin used: ```vue inspect --plugins```

