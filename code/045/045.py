import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
df['price'] = df.price / 1000
df['sea_view'] = df.view.apply(lambda x: int(x == 'Sea view'))

X = df.drop(["price", "view"], axis=1)
X = sm.add_constant(X)
y = df.price

model = sm.OLS(y, X).fit()  # Our standard form here
print(model.summary())
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                  price   R-squared:                       0.913
# Model:                            OLS   Adj. R-squared:                  0.910
# Method:                 Least Squares   F-statistic:                     335.2
# Date:                Sat, 11 Nov 2023   Prob (F-statistic):           1.02e-50
# Time:                        00:40:30   Log-Likelihood:                -1144.6
# No. Observations:                 100   AIC:                             2297.
# Df Residuals:                      96   BIC:                             2308.
# Df Model:                           3                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const      -5.398e+06   9.94e+05     -5.431      0.000   -7.37e+06   -3.43e+06
# size         223.0316      7.838     28.455      0.000     207.473     238.590
# year        2718.9489    493.502      5.510      0.000    1739.356    3698.542
# sea_view    5.673e+04   4627.695     12.258      0.000    4.75e+04    6.59e+04

plt.figure(figsize=(8, 6))
sns.lmplot(x='size', y ='price', hue='view', data = df)
plt.savefig("plot.png")
