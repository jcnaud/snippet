## OSM:

It is fully possible to use OpenStreetMap in a commercial product. The only thing we require is that you credit OpenStreetMap. However we would prefer donations and that you help making the map better.


Spesific extract with
- Osmosis
- osmconvert
- osmfilter

Custom data set
- XAPI
- Overpass API
- Export Tool

## Tileserver-gi

Source : https://github.com/maptiler/tileserver-gl
licence : https://github.com/maptiler/tileserver-gl/blob/master/LICENSE.md
Techno : JavaScript/Node.js

Normaly commercial usage OK:
 - https://support.maptiler.com/i655-commercial-usage-of-tileserver

TileServerGL : 
 - Serve Raster and Vector maps with GL style
 - Can render raster in backend
 - can generate raster from vector ?

- tileserver-gl-light (.i.e without rasterization)
 - Serve Vector maps with GL style
 - Serve Raster maps if pregenered before with GL style

tileserver-php :


## OSM2VectorTiles
- Source : https://github.com/osm2vectortiles/osm2vectortiles
- Licence : MIT
- Usage: Give opensource 
- IMPORTANT: This project have problème with MAPBOX Compagnie about schema Licence.
- SOLUTION: They say to switch to Openmaptiles.org



## openmaptiles
- Site: https://openmaptiles.org
- source code : https://github.com/openmaptiles/openmaptiles
- Schema:
 - Schema doc: https://openmaptiles.org/schema/
 - Schema SQL: https://github.com/openmaptiles/openmaptiles/tree/master/layers
 - licence:
   - Deesign CC-BY: Commercial USAGE ok  

openmaptiles-skiing
  - Usgae: create custom layer
  - source code : https://github.com/openmaptiles/openmaptiles-skiing

openmaptiles-tools
- Site: https://openmaptiles.org
- Licence: MIT
  - Code: Commercial USAGE ok  
  - Design CC-BY: Commercial USAGE ok  

## ogr2ogr

ogr2ogr:
- read:
  - xml
  - pbf
  - DBMS


## OSM Tool
url : https://hub.docker.com/r/mediagis/osmtools/
 - osmconvert - can be used to convert and process OpenStreetMap files (Ex: Crop)
  - Exemple: ./osmconvert file.pbf -o=file.o5m
 - osmfilter - is a command line tool used to filter OpenStreetMap data files for specific tags.
   - Process only .osm format and .o5m format (not .osm.pbf)
 - osmupdate - downloads and cumulates OSM Changefiles of different categories (minutely, hourly, daily).




Import OSM file to Posgresql/PostGIS:
- osm2pgsql
  - Approche par nature de géométrie:
    - Ex: table: 
      - planet_osm_line
      - planet_osm_nodes
      - planet_osm_point
      - planet_osm_polygon
- imposm
  - Approche par nature d'object
    - Ex: table: 
      - boundary
      - transportation
      - place
      - water