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

# proper data types
df['country'] = df.country.astype("category")
print(df.country.cat.categories)
# Index(['Australia', 'Austria', 'Bahrain', 'Belgium', 'Brazil', 'Canada',
#        'Channel Islands', 'Cyprus', 'Czech Republic', 'Denmark', 'EIRE',
#        'European Community', 'Finland', 'France', 'Germany', 'Greece',
#        'Hong Kong', 'Iceland', 'Israel', 'Italy', 'Japan', 'Lebanon',
#        'Lithuania', 'Malta', 'Netherlands', 'Norway', 'Poland', 'Portugal',
#        'RSA', 'Saudi Arabia', 'Singapore', 'Spain', 'Sweden', 'Switzerland',
#        'USA', 'United Arab Emirates', 'United Kingdom', 'Unspecified'],
#       dtype='object')

df.country.value_counts()
# country
# United Kingdom          495478
# Germany                   9495
# France                    8557
# EIRE                      8196
# Spain                     2533
