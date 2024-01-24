import pandas as pd

def evaluate_dq(data, column_level=True):
    info = pd.DataFrame()
    info['Dataset'] = [len(data)]
    info['Columns'] = [len(data.columns)]
    info['Missing Values'] = data.isnull().sum().sum()
    info['Duplicate Rows'] = data.duplicated().sum()
    cinfo = pd.DataFrame()
    cinfo.index = data.columns
    cinfo['Data Type'] = list(data.dtypes)
    cinfo['Missing Values'] = list(data.isnull().sum())
    cinfo['Unique Values'] = list(data.nunique())
    cinfo['Min'] = list(data.min())
    cinfo['Max'] = list(data.max())
    cinfo['Mean'] = list(data.mean())
    cinfo['Median'] = list(data.median())
    cinfo['Negative Values'] = list((data < 0).sum())
    cinfo['Zero Values'] = list((data == 0).sum())
    return (info, cinfo) if column_level else info

url = "https://archive.ics.uci.edu/ml/machine-learning-databases"
url = f"{url}/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')
df.columns = (df
    .columns.str.replace(" ", "_")
    .str.lower())

dq, column_dq = evaluate_dq(df)
print(dq)
#    Dataset  Columns  Missing Values  Duplicate Rows
# 0     1599       12               0             240

print(column_dq)
#                     Data Type  Miss  Unique   Min     Max
# fixed_acidity         float64     0      96  4.60   15.90 ...
# volatile_acidity      float64     0     143  0.12    1.58 ...
# citric_acid           float64     0      80  0.00    1.00 ...
# residual_sugar        float64     0      91  0.90   15.50 ...
# chlorides             float64     0     153  0.01    0.61 ...
# free_sulfur_dioxide   float64     0      60  1.00   72.00 ...
# total_sulfur_dioxide  float64     0     144  6.00  289.00 ...
# density               float64     0     436  0.99    1.00 ...
# ph                    float64     0      89  2.74    4.01 ...
# sulphates             float64     0      96  0.33    2.00 ...
# alcohol               float64     0      65  8.40   14.90 ...
# quality                 int64     0       6  3.00    8.00 ...