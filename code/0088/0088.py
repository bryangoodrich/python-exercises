import pandas as pd
import pyarrow.parquet as pq
import re

def underscore(word):
    """ Just import inflection.underscore! """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    return word.replace("-", "_").lower()

def is_numeric(series):
    return series.str.contains('\d+$')

def is_negative(series):
    return series < 0

dataset = "data/invoices.parquet"
df = pq.read_table(dataset).to_pandas()
df.columns = df.columns.map(underscore)  # FIX COLUMNS

df['country'] = df.country.astype("category")
df['invoice_cost'] = df.unit_price * df.quantity
df['stock_number'] = (pd
    .to_numeric(df.stock_code, errors='coerce')
    .fillna(0)
    .astype("int64"))

breakpoints = [-999_999_999, 0, 25_000, 50_000, 100_000, 999_999_999]
labels = ['negative', '0-25,000', '25,000-50,000', '50,000-100,000', '100,000+']
df['invoice_cost_bracket'] = pd.cut(
    df.invoice_cost, 
    breakpoints, 
    labels=labels, 
    ordered=True)


# sequential? invoice number or invoice dates
df = df.sort_values("invoice_date")
gap = df.loc[df.invoice_date.diff() > pd.Timedelta(days=1)]

df.groupby("country").invoice_cost.sum()

df["invoice_year"] = df.invoice_date.dt.year
dg = df.groupby(['country', 'invoice_year']).invoice_cost.sum().reset_index()
dg.pivot(index='country', 
    columns='invoice_year',
    values='invoice_cost')
# invoice_year               2010         2011
# country                                     
# Australia               1005.10   136072.170
# Austria                  257.04     9897.280
# Bahrain                  205.74      342.660
# Belgium                 1809.91    39101.050
# Brazil                     0.00     1143.600


# analyze -> repeat customers, sales by customer

def get_30day_customer_count(df, end_date):
  start_date = end_date - pd.Timedelta(days=30)
  
  df_last_30 = df[(df['invoice_date'] >= start_date) &  
                  (df['invoice_date'] <= end_date)]
                  
  unique_cust_30d = df_last_30['customer_id'].unique()
  
  num_cust_30d = len(unique_cust_30d)
  
  return num_cust_30d

# Example usage:
end_date = '2023-01-15'
num_cust = get_30day_customer_count(df, end_date)