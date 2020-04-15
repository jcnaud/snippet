# Python 3


**UNDER CONSTRUCTION**

## Install python3

### On windows 10


### On linux

Source :
 - https://virtualenvwrapper.readthedocs.io/en/latest/install.html
 - https://docs.python-guide.org/dev/virtualenvs/

pip3 install --user --upgrade virtualenv
mkdir $HOME/python_env
cd $HOME/python_env
virutalenv -p `which python3` venv


Each time you want to use this environnement, use:
```bash
mkdir SOME_DIR
source venv/bin/activate
```

You can also exit this environnement with:
```bash
deactivate
```

sudo pip install virtualenvwrapper

Add in .bashrc
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

chmod o+rx /usr/local/bin/virtualenvwrapper.sh



workon
mkvirtualenv

virtualenv -p /usr/bin/python2.7 venv


mkvirtualenv ansible

~/Envs.

workon project_folder





```bash
sudo pip3 install virtualenv virtualenvewrapper

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
```