
library(rgdal)

a <- 'Je m\'appelle Philippe.'
print(a)

library(maptools)
geol = readShapeSpatial("cal.shp")
plot(geol)
axis(1);axis(2):bbox()
