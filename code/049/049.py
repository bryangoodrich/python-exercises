import pandas as pd

url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)

avg_by_pcls_sex = df.groupby(['Pclass', 'Sex']).agg(Fare=('Fare', 'mean')).reset_index()
avg_by_pclass = df.groupby(['Pclass']).agg(Fare=('Fare', 'mean')).reset_index()
avg_by_sex = df.groupby(['Sex']).agg(Fare=('Fare', 'mean')).reset_index()
avg_fare = df.agg(Fare=('Fare', 'mean'))

grouping_sets = [avg_by_pcls_sex, avg_by_pclass, avg_by_sex, avg_fare]
result = pd.concat(grouping_sets, ignore_index=True)
print(result)
#     Pclass     Sex        Fare
# 0      1.0  female  106.125798
# 1      1.0    male   67.226127
# 2      2.0  female   21.970121
# 3      2.0    male   19.741782
# 4      3.0  female   16.118810
# 5      3.0    male   12.695466
# 6      1.0     NaN   84.154687
# 7      2.0     NaN   20.662183
# 8      3.0     NaN   13.707707
# 9      NaN  female   44.479818
# 10     NaN    male   25.633935
# 11     NaN     NaN   32.305420