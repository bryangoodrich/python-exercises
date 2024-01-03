import pandas as pd
import pyarrow.parquet as pq

TYPE_MAP = {
    "object": "Text",
    "int64": "Whole Number",
    "int32": "Whole Number",
    "float64": "Decimal Number",
    "float32": "Decimal Number",
    "datetime64[ms]": "Date and Time",
    "datetime64[ns]": "Date and Time",
    "bool": "True or False",
    "category": "Categorical"
}

dataset = "data/invoices.parquet"
df = pq.read_table(dataset).to_pandas()


dtypes = df.dtypes.items()
fields = {
    col: TYPE_MAP.get(str(dtype), "Unknown") 
    for col, dtype in dtypes
}

null_counts = df.isnull().sum()
total_count = len(df)
pct_nulls = (null_counts / total_count) * 100

summary = pd.DataFrame({
    "types": fields.values(),
    "nulls": null_counts,
    "pct_null": round(pct_nulls, 2),
}, index=fields.keys())
print(summary)
#                       types   nulls  pct_null
# InvoiceNo              Text       0      0.00
# StockCode              Text       0      0.00
# Description            Text       0      0.00
# Quantity       Whole Number       0      0.00
# InvoiceDate   Date and Time       0      0.00
# UnitPrice    Decimal Number       0      0.00
# CustomerID   Decimal Number  135080     24.93
# Country                Text       0      0.00

print(df.describe())
#             Quantity                 InvoiceDate      UnitPrice     CustomerID
# count  541909.000000                      541909  541909.000000  406829.000000
# mean        9.552250  2011-07-04 13:34:57.156000       4.611114   15287.690570
# min    -80995.000000         2010-12-01 08:26:00  -11062.060000   12346.000000
# 25%         1.000000         2011-03-28 11:34:00       1.250000   13953.000000
# 50%         3.000000         2011-07-19 17:17:00       2.080000   15152.000000
# 75%        10.000000         2011-10-19 11:27:00       4.130000   16791.000000
# max     80995.000000         2011-12-09 12:50:00   38970.000000   18287.000000
# std       218.081158                         NaN      96.759853    1713.600303
