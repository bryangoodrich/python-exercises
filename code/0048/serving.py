import pandas as pd
import pyarrow.parquet as pq
import redis

from fastapi import FastAPI

pool = redis.ConnectionPool(host='localhost', port=6379)
db = redis.Redis(connection_pool=pool)

app = FastAPI()

@app.get('/data/{site}')
def get_data(site: str):
   batch = (pq
      .read_table("batch_data.parquet")
      .to_pandas()
      .query(f"site == '{site}'"))
   bytestr = db.get('streaming_data')
   stream = pd.read_json(bytestr.decode("utf-8"))
   return {'batch': batch, 'stream': stream}
