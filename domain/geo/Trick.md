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

## Exmaple

### Self hosted OSM OpenMapTiles

- url: https://golb.hplar.ch/2018/07/self-hosted-tile-server.html