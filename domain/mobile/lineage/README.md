# Lineage 



## Link: 

https://www.lineageosrom.com/2017/01/how-to-build-lineageos-rom-for-any.html
https://en.wikibooks.org/wiki/Advanced_phone_customization/Building_your_own_ROM


## Preinstall

```bash
apt install python git
git config --global user.email "xxxxxx"
git config --global user.name "xxxxxx"
```

## Install

### Get adb and fastboot

Download here: https://developer.android.com/studio/releases/platform-tools

You will have platform-tools_xxxx.zip file

```bash
mkdir -p tools
cd tools
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
mkdir -p ~/usr
unzip platform-tools-latest-linux.zip -d ~/usr

ls -l ~/usr
cd ..
rm -rf tools
```

In your ~/.profile, add
```bash
# add Android SDK platform tools to path
if [ -d "$HOME/usr/platform-tools" ] ; then
    PATH="$HOME/usr/platform-tools:$PATH"
fi
```

Close and reopen your terminal

```bash
# Check
adb --version
fastboot --version

# 
sudo apt update
sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-gtk3-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev
```

```bash
# Make directory will contained git-repo tool (commonly named “repo”) 
mkdir -p ~/bin
# Make directory will contain the source code of LineageOS.
mkdir -p ~/android/lineage

# Install the "repo"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```

Put the ~/bin directory in your path of execution


vim ~/.bashrc
```bash
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

export USE_CCACHE=1
export CCACHE_EXEC=/usr/bin/ccache
ccache -M 50G
```

```bash


# Initialize the LineageOS source repository
cd ~/android/lineage
# Change the lineage version (here lineage-17.1)
repo init -u https://github.com/LineageOS/android.git -b lineage-17.1

# Start the download
repo sync -j 3 -c
```


