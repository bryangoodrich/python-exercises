import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.ar_model as tsa

remove_dollar_sign = lambda v: float(v.replace('$', '').replace(',', ''))

url = "https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master/Dow%20Jones%20Index/dow_jones_index.data"
raw = pd.read_csv("data/dow_jones_index.data", converters={"close": remove_dollar_sign})
raw['ar1'] = raw.close.shift(1)
data = sm.add_constant(raw.dropna())  # AutoReg can do this for you!
X = sm.add_constant(data[['volume', 'ar1']])
y = data.close
model1 = sm.OLS(data.close, X).fit()
model2 = tsa.AutoReg(y, lags=1, exog=X.volume).fit()

#                             OLS Regression Results                                                           
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         13.1986      1.351      9.772      0.000      10.547      15.850
# volume     -3.208e-08   3.91e-09     -8.208      0.000   -3.98e-08   -2.44e-08
# ar1            0.8250      0.018     45.711      0.000       0.790       0.860
# ==============================================================================

#                             AutoReg Model Results                             
# ==============================================================================
#                  coef    std err          z      P>|z|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         13.2293      1.350      9.796      0.000      10.582      15.876
# volume     -3.211e-08    3.9e-09     -8.227      0.000   -3.98e-08   -2.45e-08                                   
# close.L1       0.8247      0.018     45.714      0.000       0.789       0.860
# =============================================================================
#                   Real          Imaginary           Modulus         Frequency
# -----------------------------------------------------------------------------
# AR.1            1.2126           +0.0000j            1.2126            0.0000
# -----------------------------------------------------------------------------
