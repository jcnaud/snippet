###


- Get OSM data
- Convert to mbtiles
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