# github.com/bryangoodrich/python-exercises
# code/0017/0017.py

# %% Imports
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.api import qqplot
from scipy.stats import kstest
import pandas as pd

# %% Load the Red Wine Quality dataset from UCI and Fit OLS Model
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')
df.columns = df.columns.str.replace(' ', '_')  # snake_case
model = ols("quality ~ " + " + ".join(df.columns[:-1]), data=df).fit()
residuals = model.resid

# %% Residual Scatter Plot
plt.scatter(range(len(residuals)), residuals, color="#CCCCCC", s=10)
plt.axhline(y=0, color="red")
plt.savefig("scatter.png")

# %% Residual Histogram
plt.hist(residuals, bins=15, alpha=0.7, color='#CCCCCC', edgecolor="black")
plt.axvline(x=0, color="red")
plt.savefig("histogram.png")

# %% Residual QQ Plot for Normality
qqplot(residuals, line='q')
plt.savefig("qqplot.png")

# %% Perform Kolmogorov-Smirnov test for normality
ks_statistic, ks_p_value = kstest(residuals, 'norm')
print('Kolmogorov-Smirnov test for normality:')
print(f'KS Statistic: {ks_statistic}')
print(f'P-value: {ks_p_value}')
# Kolmogorov-Smirnov test for normality:
# KS Statistic: 0.13239369299046236
# P-value: 6.69698867739247e-25
