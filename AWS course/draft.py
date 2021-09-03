import scipy.stats
from scipy.stats import binom

x = scipy.stats.norm(180, 34).cdf(120)
y = scipy.stats.norm(180, 34).cdf(155)
#print y - x
prob = binom.pmf(7, 60, .15)
print prob
