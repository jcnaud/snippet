###


- Get OSM data  (geofabrik))
- Import OSM data in postgresql database (ipmosm)
- Convert DB to mbtiles
- run vector tile server
- use client js

- sourve: https://github.com/openmaptiles/openmaptiles-skiing

It use in sub tools: import-iosm MIT : https://github.com/openmaptiles/import-osm

Init project
```bash
git clone git@github.com:openmaptiles/skiing.git
cd openmaptiles
# Build the imposm mapping, the tm2source project and collect all SQL scripts
make
```

Run database
```bash
docker-compose up -d postgres
```

Get OSM data (Europe = 20G)
```bash
cd data
wget http://download.geofabrik.de/europe-latest.osm.pbf
wget http://download.geofabrik.de/europe/france/bretagne-latest.osm.pbf
```

Put OSM data pbf to postgresql using ```build/mapping.yaml```` created by make
```bash
docker-compose run import-osm
```

(Optioon) If you update layer SQL you need ot run 
```bash
make clean
make
docker-compose run import-sql
````

Generate Vector tile form data in Postgresql
```bash
docker-compose run generate-vectortiles
```
Or check /openmaptiles/openmaptiles-tools

Run tileserver-gl
```bash
sudo docker run -d --restart unless-stopped -v /opt/maps:/data -p 10001:80 klokantech/tileserver-gl
```


//sudo npm install --unsafe-perm=true -g tileserver-gl-light







## === Test real  ===


Get OSM Bretagne (250 Mo)
```bash
mkdir data
cd data
wget http://download.geofabrik.de/europe/france/bretagne-latest.osm.pbf
cd ..
```

Get openmaptiles-tools (MIT License)
```
git clone https://github.com/openmaptiles/openmaptiles-tools.git
cd openmaptiles-tools
git checkout v4.0.0
```



docker run -it --rm -u $(id -u ${USER}):$(id -g ${USER}) \
           -v "${PWD}:/tileset" \
           openmaptiles/openmaptiles-tools \
           <script-name> <script-parameters>


      make download-geofabrik area=albania


## === Test 2 ===
https://blog.project-insanity.org/2018/10/29/host-your-own-mapbox-gl-js-vector-tiles-map/

```bash
git clone https://github.com/openmaptiles/openmaptiles.git
cd openmaptiles
make
mkdir data
wget "https://download.geofabrik.de/europe/germany/baden-wuerttemberg/karlsruhe-regbez-latest.osm.pbf"
osmconvert karlsruhe-regbez-latest.osm.pbf -b=7.893,48.73,8.816,49.246 -o=data/karlsruhe-latest.osm.pbf
sed -i "s/QUICKSTART_MAX_ZOOM=.*$/QUICKSTART_MAX_ZOOM=14/g" .env
./quickstart karlsruhe-latest
```

