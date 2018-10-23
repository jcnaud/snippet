# R

## Run R script

```bash
Rscript --no-save main.R
```

Run one command
```bash
R -e 'a <- 1'

## Install a package

Run R terminal:
```bash
R
```

Install the package with preselected repository
```r
install.package('raster', repos='http://cran.us.r-project.org')
```

## List
```R
installed.packages()
```