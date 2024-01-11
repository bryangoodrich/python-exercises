import duckdb

db = duckdb.connect()
create_query = """
CREATE TABLE invoice
AS
SELECT *
FROM read_parquet("data/invoices.parquet")
"""
db.sql(create_query)

db.sql("SELECT COUNT(1) as N from invoice")
# ┌────────┐
# │   N    │
# │ int64  │
# ├────────┤
# │ 541909 │
# └────────┘

select_qry = """
SELECT *
FROM invoice
USING SAMPLE 10%
"""
df = db.execute(select_qry).df()
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 53248 entries, 0 to 53247
# Data columns (total 8 columns):
#  #   Column       Non-Null Count  Dtype         
# ---  ------       --------------  -----         
#  0   InvoiceNo    53248 non-null  object        
#  1   StockCode    53248 non-null  object        
#  2   Description  53248 non-null  object        
#  3   Quantity     53248 non-null  int64         
#  4   InvoiceDate  53248 non-null  datetime64[us]
#  5   UnitPrice    53248 non-null  float64       
#  6   CustomerID   37851 non-null  float64       
#  7   Country      53248 non-null  object        
# dtypes: datetime64[us](1), float64(2), int64(1), object(4)
# memory usage: 3.3+ MB
