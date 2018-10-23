library(plotKML)


plotKML.env(silent = FALSE, kmz = FALSE)
## -------------- SpatialPointsDataFrame --------- ##
library(sp)
library(rgdal)

## -------------- SpatialPixelsDataFrame --------- ##
library(rgdal)
library(raster)
data(eberg_grid)
gridded(eberg_grid) <- ~x+y
proj4string(eberg_grid) <- CRS("+init=epsg:31467")
TWI <- reproject(eberg_grid["TWISRT6"])
data(SAGA_pal)
plotKML(TWI, colour_scale = SAGA_pal[[1]])
## set limits manually (increase resolution):

print("= some data =")
print(gridparameters(TWI)[1,"cells.dim"]*5)
print(gridparameters(TWI)[2,"cells.dim"]*5)

plotKML(TWI, z.lim=c(12,20), colour_scale = SAGA_pal[[1]],
  kmz = FALSE,
  open.kml = FALSE,
  png.width = gridparameters(TWI)[1,"cells.dim"]*5, 
  png.height = gridparameters(TWI)[2,"cells.dim"]*5)



