# sudo apt-get install gdal-bin
# sudo apt-get install libudunits2-dev

# install.packages("plotKML", repos='http://cran.us.r-project.org')

# source: http://gsif.isric.org/doku.php/wiki:tutorial_plotkml


library(plotKML)

data(eberg_zones)  # Import some data typicaly used by R community
plotKML(eberg_zones["ZONES"], altitude=runif(length(eberg_zones))*500)

