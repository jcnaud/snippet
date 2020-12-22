



https://gis.stackexchange.com/questions/188141/mapbox-sdk-is-it-free-if-you-host-your-own-vector-tiles


- Using Mapbox Streets vector tiles
- Using APIs such as routing or Surface.
- Hosting your own data on Mapbox
- Using Mapbox-created styles such as Mapbox Outdoors.



Tile vector serveur
vector-tiles :
## Links

Generale:

- awesome-vector-tiles : https://github.com/mapbox/awesome-vector-tiles
- Tutorial mbtiles:
  maperitive: 
    url: http://maperitive.net/docs/Commands/GenerateMBTiles.html
    description: 
      - Give explication about nmber of tiles and computing performance
      - 
- Discution about generate planet mbtiles:
  - https://github.com/openmaptiles/openmaptiles/blob/master/QUICKSTART.md#using-your-own-osm-data


Discution about slice mbtiles
  - https://www.slideshare.net/Docker/take-control-of-your-maps-with-docker

Discution merge mbtiles:
   https://stackoverflow.com/questions/58091006/best-way-to-merge-mbtiles-files-together

Discution Optimise planet generation:
  - https://stackoverflow.com/questions/57024808/optimizing-openmaptiles-and-servers-for-planet-tiles-generation
   
## Etude des licences

OSM : 
  L’Open Database License (ODbL) : https://www.lagazettedescommunes.com/208893/le-fouilli-des-licences-open-data-seclaircit-fiche-pratique/

Parsers & Generators:
openmaptiles
  url_source : https://github.com/openmaptiles/openmaptiles
  licences:
    - Code license: BSD 3-Clause License
      - Commercial use OK
    - Design license: CC-BY 4.0 : https://fr.wikipedia.org/wiki/Licence_Creative_Commonsakadoalkant
      - Commercial use OK
      - Constraints : put **© OpenMapTiles © OpenStreetMap** contributors in the map corner
   
openmaptiles Style positron:
  url_source: https://github.com/openmaptiles/positron-gl-style
  licences:
    - Code license: BSD 3-Clause License
      - Commercial use OK
    - Design license: CC-BY 4.0 : https://fr.wikipedia.org/wiki/Licence_Creative_Commons
      - Commercial use OK
      - Constraints : put **© OpenMapTiles © OpenStreetMap** contributors in the map corner
openmaptiles/openmaptiles-tools:
  url_source : https://github.com/openmaptiles/openmaptiles-tools/
  licences:
    - MIT


openmaptiles Style osm:
  url_source: https://github.com/openmaptiles/osm-liberty-gl-style
  based on Openmaptils schema:
    

openmaptiles schema
  url_doc : https://openmaptiles.org/schema/
  licence:
    - CC-BY-SA: commercial use
    - COntraints: Copy left
  

openmaptiles-skiing
  url_source: https://github.com/openmaptiles/openmaptiles-skiing
  licences:
    - Code license: BSD 3-Clause License
      - Commercial use OK
    - Design license: CC-BY 4.0 : https://fr.wikipedia.org/wiki/Licence_Creative_Commons
      - Commercial use OK
      - Constraints : put **© OpenMapTiles © OpenStreetMap** contributors in the map corner


tippecanoe:
  description:  merge mbtiles
  url_source: https://github.com/mapbox/tippecanoe
    -licence: 
      code source: BSD 2-Clause "Simplified" License
        - Commercial use OK




## Renderer

mapnik

# Style

- maputnik

## Edit
- gl-draw

## Servers
