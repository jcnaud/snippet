# sudo apt-get install gdal-bin
# sudo apt-get install libudunits2-dev

# install.packages("plotKML", repos='http://cran.us.r-project.org')

# source: http://gsif.isric.org/doku.php/wiki:tutorial_plotkml


library(plotKML)
library(sp) #  gridded()
# For:
#RasterLayer
#SpatialPixelsDataFrame
#SpatialGridDataFrame

data(eberg_grid) # Import some data typicaly used by R community
gridded(eberg_grid) <- ~x+y
proj4string(eberg_grid) <- CRS("+init=epsg:31467")

data(SAGA_pal) # Import some data typicaly used by R community
plotKML(eberg_grid["TWISRT6"], colour_scale = SAGA_pal[[1]])