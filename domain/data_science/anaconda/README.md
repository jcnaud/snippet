# Anaconda


## Install

link: https://docs.anaconda.com/anaconda/install/linux/

This document give the process to install Anaconda on linux Debina/Ubuntu with for python3

As root, on debian/ubuntu
```bash
# Install dependencies
apt update
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

# Get anaconda
# List of installer: https://www.anaconda.com/products/individual#linux
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh

# Check the hash
# List of hash on : https://docs.anaconda.com/anaconda/install/hashes/
md5sum Anaconda3-2021.05-Linux-x86_64.sh
echo "25e3ebae8905450ddac0f5c93f89c467"
sha256sum Anaconda3-2021.05-Linux-x86_64.sh
echo "2751ab3d678ff0277ae80f9e8a74f218cfc70fe9a9cdc7bb1c137d7e47e33d53"

# Run install script
bash Anaconda3-2021.05-Linux-x86_64.sh

# Your ~/.bashrc was updated
# You need to source it if your terminal is already open 
source ~/.bashrc

# Check env in conda

# Define if environnement is actived by default
conda config --set auto_activate_base False
# Or
#conda config --set auto_activate_base True

# Or manual activate with
conda activate base
```

## Run jupyter

jupyter-notebook --notebook-dir=/home/jcnaud/var/github.com/snippet/domain/data_science