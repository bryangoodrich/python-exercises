from minio import Minio

client = Minio('localhost:9000',
    access_key='58nYugf1L5Z7d9asMzU0',
    secret_key='kRhylSjFE12ABSBiTLfoYQ5qed2YvtgnoPdsCWaY',
    secure=False)

bucket = 'invoices'
data_file = 'data/invoices.parquet'
object_name = "invoices.parquet"

if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

client.fput_object(bucket, object_name, data_file)
print(f'Successfully uploaded `{object_name}` to /{bucket}')
# Successfully uploaded `invoices.parquet` to /invoices
