import pandas as pd
from statsmodels.formula.api import ols

df = pd.read_csv("data/energy-usage.csv")
model = ols("kwh ~ cdd", data=df).fit()

model.params["cdd"]
# 38.63

model.conf_int(alpha = 1-0.95)
# 31.47   45.78

model.conf_int(alpha = 1-0.80)
# 34.00   43.26

model.get_prediction({"cdd": [20, 30]}).summary_frame(alpha=0.05)
#           mean    mean_se  mean_ci_lower  mean_ci_upper  obs_ci_lower  obs_ci_upper
# 0  2359.749502  35.267532    2289.179334    2430.319670   2061.831767   2657.667237
# 1  2746.045784  68.329196    2609.319379    2882.772188   2425.938086   3066.153481

model.get_prediction({"cdd": [20, 30]}).summary_frame(alpha=0.1)
#           mean    mean_se  mean_ci_lower  mean_ci_upper  obs_ci_lower  obs_ci_upper
# 0  2359.749502  35.267532    2314.040463    2405.458541   2166.785055   2552.713948
# 1  2746.045784  68.329196    2657.486655    2834.604912   2538.708665   2953.382902