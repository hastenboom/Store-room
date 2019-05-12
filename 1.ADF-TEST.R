install.packages("mice")##缺失值处理
install.packages("plm")
install.packages("MSBVAR")
install.packages("xts")
install.packages("tseries")

library(plm)
library(MSBVAR)
library(tseries)
library(xts) 


tlist1=xts(eview$NII,as.Date(eview$Year))
adf.test(tlist1)

tlist2=xts(eview$ROA,as.Date(eview$Year))
adf.test(tlist2)

tlist3=xts(eview$LNSIZE,as.Date(eview$Year))
adf.test(tlist3)

tlist4=xts(eview$LNGDP,as.Date(eview$Year))
adf.test(tlist4)
