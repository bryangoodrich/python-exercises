import pandas as pd
import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
redis_conn = redis.Redis(connection_pool=pool)
stream_data = pd.read_csv("weather.csv")
redis_conn.set('stream_data', stream_data.to_json())
