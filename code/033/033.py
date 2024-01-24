import pandas as pd

workbook = "data/linkedin.xlsx"
sheet = "Data"
id_vars = ["Post", "Category"]

df = pd.read_excel(workbook, sheet_name=sheet)
df = pd.melt(df, id_vars=id_vars,
        var_name="group", value_name="values")

df[['engagement', 'impressions']] = df['values'].str.split(';', expand=True).astype(float)
df[['engagement', 'impressions']] = df[['engagement', 'impressions']].fillna(0)
df['engagement_ratio'] = (df['engagement'] / df['impressions'] * 100).fillna(0)

cat = df.groupby("Category")[["impressions", "engagement"]].sum()
cat["engagement_ratio"] = cat.engagement / cat.impressions * 100
#                         impressions  engagement  engagement_ratio
# Category                                                         
# Analytics and Modeling      16997.0        80.0          0.470671
# Data Engineering            33253.0       139.0          0.418007
# Data Viz and Maps           37379.0       163.0          0.436074
# Machine Learning            26754.0       161.0          0.601779
# Programming                 85309.0       310.0          0.363385
# Statistics                  19022.0        91.0          0.478393
# Wildcard                    21197.0       104.0          0.490635


grp = df.groupby("group")[["impressions", "engagement"]].sum()
grp["engagement_ratio"] = grp.engagement / grp.impressions * 100
#                   impressions  engagement  engagement_ratio
# group                                                      
# Artificial Intel      23934.0       179.0          0.747890
# Data Scientist         9945.0        76.0          0.764203
# DevOps                15276.0        42.0          0.274941
# Machine Learning      18519.0        79.0          0.426589
# PySpark                1172.0         6.0          0.511945
# Python Community     171065.0       666.0          0.389326