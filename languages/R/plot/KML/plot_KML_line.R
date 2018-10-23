# sudo apt-get install gdal-bin
# sudo apt-get install libudunits2-dev

# install.packages("plotKML", repos='http://cran.us.r-project.org')

# source: http://gsif.isric.org/doku.php/wiki:tutorial_plotkml


library(plotKML)

data(eberg_contours)  # Import some data typicaly used by R community
plotKML(eberg_contours)