import scipy.stats
from scipy.stats import binom

# probability density function
# calculates P of < 120, < 150, then betwwen
x = scipy.stats.norm(180, 34).cdf(120)
y = scipy.stats.norm(180, 34).cdf(155)
#print y - x


# binomial distribution
# p = .15 n = 60 x = 7
prob = binom.pmf(7, 60, .15)
print prob
