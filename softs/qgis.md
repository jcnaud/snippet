# QGIS 3.4



## Install

Source : https://www.qgis.org/fr/site/forusers/alldownloads.html#debian-ubuntu


Ajouter :
```bash
sudo sh -c 'echo "deb http://qgis.org/ubuntu-ltr bionic main" > /etc/apt/sources.list.d/qgis.list'
sudo sh -c 'echo "deb-src http://qgis.org/ubuntu-ltr bionic main" >> /etc/apt/sources.list.d/qgis.list'


wget -O - http://qgis.org/downloads/qgis-2017.gpg.key | gpg --import
gpg --fingerprint CAEB3DC3BDF7FB45
gpg --export --armor CAEB3DC3BDF7FB45 | sudo apt-key add -
```

```bash
sudo apt-get install qgis
```


## Plugin to install
Usage general:
- QuickOSM

Plugin for dev :
- Plugin Builder 3
- First Aid
- Plugin Reloader (experimental)

Plugin for export
- Qgis2threejs
- qgis2web
- Batch Hillshader

Plugin to test:
- Plugin load times

## Plugin directory
%userprofile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
## Plugin natif processing directory:
C:\var\install\QGIS 3.4\apps\qgis\python\plugins\processing\algs


# QGIS 2.18

Usage general:
- OpenLayer Plugin
- QuickOSM

Plugin for dev :
- Plugin Builder
- First Aid
- Plugin Reloader (experimental)

## Plugin directory
%userprofile%\.qgis2\python\plugins

## Plugin natif processing directory:
C:\var\install\QGIS 2.18\apps\qgis-ltr\python\plugins\processing\algs
