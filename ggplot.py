from plotnine import ggplot, geom_point, aes, stat_smooth
from plotnine.data import mtcars

mtcars.head()


(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
