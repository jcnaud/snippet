# source: https://beckmw.wordpress.com/2013/01/07/breaking-the-rules-with-spatial-correlation/

#import relevant packages
library(gstat)
library(sp)
library(nlme)

#create simulated data, lat and lon from uniformly distributed variable, exp1 and exp2 from random normal
set.seed(2)  # Enble speudo random (in order to reproduce the same result multiple times)
samp.sz<-400 # Const: number of observation
lat<-runif(samp.sz,-4,4) # random uniformly distributed variable beetween -4 and 4
lon<-runif(samp.sz,-4,4)
exp1<-rnorm(samp.sz) # random normal
exp2<-rnorm(samp.sz)

#resp is linear combination of explanatory variables plus an error term that is normally distributed
resp<-1+4*exp1-3*exp2-2*lat+rnorm(samp.sz)

#pair plots of variables
plot(data.frame(resp,exp1,exp2,lat))

#correlation between variables
cor(data.frame(resp,exp1,exp2,lat))

#get mods, check parameter values with actual, but we don't know spatial correlation with lat
mod<-lm(resp~exp1+exp2) # Estimate exp1, exp2 + Const
coefficients(summary(mod))

#function for testing parameter values against actual
t_test<-function(x.bar,mu,se,deg.f,return.t=F){
  if(return.t) return(round((x.bar-mu)/se,3))
  pt(abs((x.bar-mu)/se),deg.f,lower.tail=F)*2
  }

#for first explanatory variable
t_test(3.8314, 4, 0.2534, 397)

#evidence of spatial correlation using bubble plot
dat<-data.frame(lon,lat,resids=resid(mod))
coordinates(dat)<-c('lon','lat')
bubble(dat,zcol='resids')

#evidence of spatial correlation using variogram
var.mod<-variogram(resids~1,data=dat,alpha=c(0,45,90,135))
plot(var.mod)

#refit model with correlation structure
mod.cor<-gls(resp~exp1+exp2,correlation=corGaus(form=~lat,nugget=TRUE))
summary(mod.cor)