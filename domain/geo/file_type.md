## File type describe 

- GeoJson
- GPX
- KML
- Données brute
- CSV
- Shapefile


- mbtiles



## GL Style:
- Maintainer: Mapbox
- Base: JSON
- Usage : Define style and where is Vector and Raster map API for mapbox-gl-js for example. 
- Licence: MIT or BSD claud-3 or, Apache  (Cormercial user OK if self created !!)
  - The specification of GL style is in the https://github.com/mapbox/mapbox-gl-js project
- 

## TileJSON
- Maintainer: Mapbox
- Base: JSON
- Usage : Describe maps
- Exemple : 
  - OpenLayer use TileLayer with TileJSON to create layer : https://openlayers.org/en/latest/examples/tilejson.html


## PBF ("Protocolbuffer Binary Format)
- primarily intended as an alternative to the XML format (50% ligther or 30% ligther than xml zipped)


| Command | Description |
|- |- |
| Crop | ```osmconvert karlsruhe-regbez-latest.osm.pbf -b=7.893,48.73,8.816,49.246 -o=data/karlsruhe-latest.osm.pbf``` |