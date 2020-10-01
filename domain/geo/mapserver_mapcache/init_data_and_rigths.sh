#!/bin/bash
# Init data and rights



# Download tutorial data to ./data/mapserver/ms4w if not present
if [ ! -d ./data/mapserver/ms4w ]; then 
  cd data/mapserver
  wget https://download.osgeo.org/mapserver/docs/mapserver-tutorial.zip 
  unzip mapserver-tutorial.zip
  rm mapserver-tutorial.zip
  find ./data/mapserver/ms4w -type d -exec chmod o+rx {} \;
  find ./data/mapserver/ms4w -type f -exec chmod o+r {} \;
fi;

