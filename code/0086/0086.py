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
df.columns = df.columns.map(underscore)

# enrichment
df['invoice_cost'] = df.unit_price * df.quantity
df['stock_number'] = (pd.to_numeric(df.stock_code, errors='coerce')
    .fillna(0)
    .astype("int64"))

df['country'] = df.country.astype("category")


# relationships / associations (stock code to description)

# cut into categories (quantity? total sales?)
breakpoints = [-999_999_999, 0, 25_000, 50_000, 100_000, 999_999_999]
labels = ['negative', '0-25,000', '25,000-50,000', '50,000-100,000', '100,000+']
df['invoice_cost_bracket'] = pd.cut(
    df.invoice_cost, 
    breakpoints, 
    labels=labels, 
    ordered=True)
df.invoice_cost_bracket.value_counts()
# invoice_cost_bracket
# 0-25,000          530101
# negative           11805
# 25,000-50,000          1
# 50,000-100,000         1
# 100,000+               1

# Exploration and analysis
is_numeric(df.invoice_no).sum()  # 541_909 (100%)
is_numeric(df.stock_code).sum()  # 487_234 (89.91%)

df.unit_price.map(is_negative).sum()  #      2 (~0.00%)
df.quantity.map(is_negative).sum()    # 10_624 (1.96%)

# validation? -> Customer across country?
# sequential? invoice number or invoice dates

# analyze -> timing of sales (time zones?)
# returns? 
# analyze -> sales by country
# analyze -> repeat customers, sales by customer
# analyze -> inflation? 
