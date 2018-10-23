# sudo apt-get install gdal-bin
# sudo apt-get install libudunits2-dev

# install.packages("plotKML", repos='http://cran.us.r-project.org')

# source: http://gsif.isric.org/doku.php/wiki:tutorial_plotkml


library(plotKML)
library(sp)  # function : coordinates(), ssplot()

data(eberg)  # Import some data typicaly used by R community

print('= names =')
names(eberg) # list the variables (here, dispaly column names)

print('= str =')
str(eberg)  # list the structure  (here, dispaly column names, types and some data)

print('= typeof =')
typeof(eberg) # this is a list

print('= dim =')
dim(eberg) # dimensions of an object

coordinates(eberg) <- ~X+Y  # Define X and Y as coordonates in the object (so become S4 object)
proj4string(eberg) <- CRS("+init=epsg:31467") # Add projection systeme

print('= typeof =')
typeof(eberg) # this is a S4 generic object

print('= show =')
show(eberg) # Show description


eberg <- eberg[runif(nrow(eberg))<.2,]
bubble(eberg["CLYMHT_A"])
# or
#spplot(eberg["CLYMHT_A"], edge.col="black", alpha=0.8, cex=seq(.3,3,length=5))


plotKML(eberg["CLYMHT_A"])

#setwd('/folder/where/the/file/is/')
#source('plot_KML.R')
