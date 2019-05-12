#declaring normal
normal.lik=function(pars,x)
{
  mu=pars[1]
  sigma2=pars[2]
  logl=0
  for(i in 1:length(x))
  {
    logl=logl+log(1/(sqrt(2*pi*sigma2))*exp(-(x[i]-mu)^2/(2*sigma2)))
  }
  return(-logl)
}

x=rnorm(200,mean=2,sd=6)
result=optim(c(1,1),normal.lik,x=x)


#declaring poision  
