import pandas as pd
from statsmodels.formula.api import ols

quartet = pd.DataFrame({
    "x": [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
    "y": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
})

model = ols("y ~ x", quartet).fit()
model.summary()
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.667
# Model:                            OLS   Adj. R-squared:                  0.629
# Method:                 Least Squares   F-statistic:                     17.99
# Date:                Sat, 30 Sep 2023   Prob (F-statistic):            0.00217
# Time:                        03:44:08   Log-Likelihood:                -16.841
# No. Observations:                  11   AIC:                             37.68
# Df Residuals:                       9   BIC:                             38.48
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      3.0001      1.125      2.667      0.026       0.456       5.544
# x              0.5001      0.118      4.241      0.002       0.233       0.767