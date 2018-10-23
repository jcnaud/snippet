library(rgdal)    #manipulation spatial data (readOGR, writeOGR, ...)
library(raster)

path_shape_input = "/home/jnaud/tmp/17_ariase/sshfs/ariase/ariase-interpolation/pregenered/shp_dep"
fontcolor <- "grey"
border_color <- "black"


# With "readOGR" from "rgdal" library
#   arg: Path + file name without extention
shape1 <- readOGR("/home/jnaud/tmp/17_ariase/sshfs/ariase/ariase-interpolation/pregenered/shp_dep", "dep_75")
print(shape1)
plot(shape1 , col=fontcolor, border=border_color)


# With "shapefile" from "raster" library
#   arg: full path name
shape2 <- shapefile("/home/jnaud/tmp/17_ariase/sshfs/ariase/ariase-interpolation/pregenered/shp_dep/dep_75.shp")
print(shape2)
plot(shape2 , col=fontcolor, border=border_color)

# Without marging
par(mar=c(0,0,0,0))
plot(shape2 , col=fontcolor, border=border_color)
dev.off()

# # With reprojection
# shape3<-spTransform(shape2, CRS("+init=epsg:2154"))
# print(shape3)
# plot(shape3 , col=fontcolor, border=border_color)
