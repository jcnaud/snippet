# tippecanoe

##
Link : https://openmaptiles.org/docs/generate/custom-vector-from-shapefile-geojson/

Reprojection and convertion ShapeFile  to EPSG:4326 GEOJSON

```bash
ogr2ogr -f GeoJSON your_data_in_4326.json -t_srs EPSG:4326 your_data.shp
```

Convert json  EPSG:4326 to mbtiles wit zoom 0 to 14
```bash
tippecanoe -o your_data.mbtiles your_data_in_4326.json
```

Run tileServer-GL(docker) with our mbtiles
```bash
docker run -it -v $(pwd):/data -p 8080:80 klokantech/tileserver-gl your_data.mbtiles
````





## Keep local OSM database sync

- url: https://ircama.github.io/osm-carto-tutorials/updating-data/
- Tools:
  - Osmosis, a command line Java application with pluggable components for downloading and processing OSM data, generate dumps and apply change sets to a database;
  - Osmconvert, a command line tool written in C allowing fast conversion and processing of different OpenStreetMap data formats;
  - Osmupdate, a small and fast a command line tool written in C to download and assemble OSM Changefiles;
  - Osmfilter, a command line tool used to filter OpenStreetMap data files for specific tags;
  - Osmium, a multipurpose command line tool to work with OpenStreetMap data files, convert OSM files formats, merge and apply change files;
  - Imposm, a full-featured importer for PBF OpenStreetMap data to PostgreSQL/PostGIS written in GO which can also automatically update the database with the latest changes from OSM.

## Example

### Self hosted OSM OpenMapTiles

- url: https://golb.hplar.ch/2018/07/self-hosted-tile-server.html

https://blog.project-insanity.org/2018/10/29/host-your-own-mapbox-gl-js-vector-tiles-map/


```bash
git clone https://github.com/openmaptiles/openmaptiles.git
cd openmaptiles
git checkout v3.11
make
mkdir data_download 
wget http://download.geofabrik.de/europe/france/bretagne-latest.osm.pbf -O /data_download/osm-data/bretagne-latest.osm.pbf
```


Check data statistic
```bash
docker run --rm  -it --volume "${PWD}/data_download:/osm" mediagis/osmtools osmconvert --out-statistics bretagne-latest.osm.pbf
```
See more at : 
- https://hub.docker.com/r/mediagis/osmtools/  (osmconvert, osmfilter, osmupdate)
- https://nominatim.openstreetmap.org/
- https://www.openstreetmap.org/
- https://boundingbox.klokantech.com/

Get the BBox of Rennes
```bash
docker run --rm  -it --volume "${PWD}/data_download:/osm" mediagis/osmtools /bin/bash
osmconvert bretagne-latest.osm.pbf -o=bretagne-latest.o5m
osmfilter bretagne-latest.o5m --keep="admin_level=8 and boundary=administrative and name=Rennes" -o=rennes_boundary.osm
osmconvert --out-statistics rennes_boundary.osm
```

We obtain the statistics about one relation and you have the BBox of rennes :
lon min: -1.7525876
lon max: -1.6244045
lat min: 48.0769155
lat max: 48.1549705


Filter the pbf to extract the citi zone:
```bash
osmconvert bretagne-latest.osm.pbf -b=-1.7525876,48.0769155,-1.6244045,48.1549705 -o=rennes.osm.pbf
```

Check result .i.e number of relation and BBox.
```bash
osmconvert --out-statistics rennes.osm.pbf
chmod 666 rennes.osm.pbf
```

Go out of the docker with ```exit```

```bash
mkdir data
mv data_download/rennes.osm.pbf data/rennes.osm.pbf

sed -i "s/QUICKSTART_MAX_ZOOM=.*$/QUICKSTART_MAX_ZOOM=14/g" .env
./quickstart.sh rennes
```

To avoid bug

vim ./data/docker-compose-config.yml
```yml
version: "2"
services:
  generate-vectortiles:
    environment:
      BBOX: "-1.7525876, 48.0769155, -1.6244045, 48.1549705 "
      OSM_MAX_TIMESTAMP : "2020-04-01T20:54:00Z"
      OSM_AREA_NAME: "rennes"
      MIN_ZOOM: "0"
      MAX_ZOOM: "14"
```



## TODO

https://makina-corpus.com/blog/metier/2019/tour-d-horizon-des-serveurs-de-tuiles-vectorielle-pour-fond-de-carte
