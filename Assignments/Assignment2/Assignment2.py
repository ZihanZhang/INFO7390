import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import time
np.random.seed(seed=int(time.time()))

# Make plots larger
plt.rcParams['figure.figsize'] = (15, 9)


# Question2
domain = np.arange(-30, 30, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
left = np.arange(-30, -20, 0.1)
lefts = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

domain = np.arange(-30, 30, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
right = np.arange(20, 30, 0.1)
rights = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

domain = np.arange(-30, 30, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.fill_between(right, 0, rights, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

result1 = stats.norm(0,1).cdf(-20)
result2 = result1
result3 = result1 + result2



# Question4
domain = np.arange(-100, 100, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
left = np.arange(-100, -63.24, 0.1)
lefts = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

domain = np.arange(-100, 100, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
right = np.arange(63.24, 100, 0.1)
rights = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

domain = np.arange(-100, 100, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.fill_between(right, 0, rights, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

result1 = stats.norm(0,1).cdf(-63.24)
result2 = result1
result3 = result1 + result2

# Question6
domain = np.arange(-5, 5, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
left = np.arange(-5, -1.884382659765678, 0.1)
lefts = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()
result = stats.norm(0,1).cdf(-1.884382659765678)

# Question8
domain = np.arange(-5, 5, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
left = np.arange(1,01, 5, 0.1)
lefts = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

levelz = stats.norm(0, 1).ppf(0.05)
result = stats.norm(0,1).cdf(-1.01)

# Question10
domain = np.arange(-5, 5, 0.1)
values = stats.norm(0, 1).pdf(domain)
plt.plot(domain, values, color='r', linewidth=2)
left = np.arange(-5, -0.7453559924999299, 0.1)
lefts = stats.norm(0, 1).pdf(left)
plt.fill_between(left, 0, lefts, color='grey', alpha = 0.5)
plt.ylabel("Probability")
plt.title("Normal Distributions")
plt.show()

levelz = stats.norm(0, 1).ppf(0.025)
result = stats.norm(0,1).cdf(-0.7453559924999299)

interval = [101 - 1.96*60/pow(500, 1/2), 101 + 1.96&60/pow(500, 1/2)]
