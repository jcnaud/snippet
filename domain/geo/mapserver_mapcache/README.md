# Mapserver Mapcache


## Mapserver

### Links

- [ ] https://mapserver.org/fr/introduction.html


### Input data
Data can be compiled with GDAL(Raster) and OGR(vector).


Vector data: https://mapserver.org/fr/input/vector/index.html#vector
Raster data: https://mapserver.org/fr/input/raster.html#raster

Different kind of source are avalaible:
- [ ] Vector data
- [ ] Raster data
- [ ] WMS
- [ ] WFS
- [ ] Tiles web service

### Inside mapserver

- Configuration files *.map
- Mapserver CGI Application && MapScipt Application
- Apache with cgi

### Ouput data

- SWF
- SVG
- PDF
- HTML + images
- images
- WMS
- WFS
- WCS





### Tutorial


Run ```./init_data_and_rigths.sh``` to download and init data


#### Example 1.1 : Simple vector map

Doc: https://mapserver.org/fr/tutorial/example1-1.html#example1-1

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-1.map&layer=states&mode=map


#### Example 1.2 : Multi layer

SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities ?


Doc: https://mapserver.org/fr/tutorial/example1-2.html#example1-2

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-2.map&layer=states_poly&layer=states_line&mode=map


#### Example 1.3 : Multi class in layer

Doc: https://mapserver.org/fr/tutorial/example1-3.html#example1-3

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-3.map&layer=states_poly&layer=states_line&mode=map

#### Example 1.4 : Label

Doc: https://mapserver.org/fr/tutorial/example1-4.html#example1-4

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-4.map&layer=states_poly&layer=states_line&mode=map

#### Example 1.5: Raster layer

Doc: https://mapserver.org/fr/tutorial/example1-5.html#example1-5

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-5.map&layer=states&layer=modis&layer=states_line&mode=map

#### Example 1.6: Proj

Doc: https://mapserver.org/fr/tutorial/example1-6.html#example1-6

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-6.map&layer=states&layer=modis&layer=states_line&mode=map

#### Example 1.7: Add OGC WMS layers

Doc: https://mapserver.org/fr/tutorial/example1-7.html#example1-7

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-7.map&layer=states&layer=modis_nasa&layer=states_line&mode=map

#### Example 1.8: Change format

Doc: https://mapserver.org/fr/tutorial/example1-8.html#example1-8

url:
- http://localhost/cgi-bin/mapserv?map=/ms4w/apps/tutorial/htdocs/example1-8.map&layer=states&layer=modis&layer=states_line&mode=map

#### Example 1.9: Interactive map

Doc: https://demo.mapserver.org/cgi-bin/mapserv?map=/osgeo/mapserver/tutorial/htdocs/example1-9.map&layer=states&layer=modis&program=https://demo.mapserver.org/cgi-bin/mapserv



