# Git

## Install git
### On windows 10

Download and install git : [git-scm.com](git-scm.com)

Install PuTTY to allow ssh key management : https://www.putty.org/
- Go to Download PuTTY
- Download the MSI (‘Windows Installer’)

Add environnement variable: **GIT_SSH** ```C:\Program Files\PuTTY\plink.exe```

Before using serveur, you need to valid/import the public key with **plink** but not with **putty**  
Example with [www.github.com](www.github.com)

```cmd
C:\Program Files\PuTTY\plink.exe www.github.com
-> yes
```

You need to do this because  :
- **putty.exe** save server public key in **.ssh/knows_hosts** and use this standard ssh connection
- **plink** save server public key in an other place.


To avoid multiple password entry, use **pagent.exe** and import the key (with windowsformat (ppk)). If the key is not in the good format or if you don't have your private key, use **puttygen.exe** to convert or create it.


## Extensions
### Git Large File Storage (LFS):

LFS manage heavy commited file, the goal is to save these files in an other space disk on the server.

Install LFS [https://git-lfs.github.com/](https://git-lfs.github.com/)


After, for each project, you need to initialize it one time.
```git bash
git lfs install
```

LFS files are configurate with **.gitattribute** file.
You can auto create this file with this command:

```cmd
git lfs track "*.csv"
```

Display **.gitattribute**:
```
*.csv filter=lfs diff=lfs merge=lfs -text
```
Add all of it.
```
git add .gitattribute
git add *.csv
```
Display files managed by LFS:
```
git lfs ls-files
```
files managed by LFS are also display in ```git status```
