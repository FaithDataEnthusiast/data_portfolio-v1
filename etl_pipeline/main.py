import os
import pandas as pd
# from dotenv import load_dotenv

# load_dotenv()  # only for local testing
from src.extract import extract_transactional_data
from src.transform import removing_duplicate_data
# from src.transform import convert_datatype_to_datetime
from src.load_data_to_s3 import df_to_s3

dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("sh_aws_access_key_id")
aws_secret_access_key = os.getenv("sh_aws_secret_access_key")

# extract data
online_transaction = extract_transactional_data(dbname, host, port, user, password)
print(type(online_transaction))
# print(online_transaction.head())

# transform data
online_transaction_clean = removing_duplicate_data(online_transaction)

# online_transaction_clean = convert_datatype_to_datetime(online_transaction_clean, 'invoice_date')
# print(online_transaction_clean.info())

# fix the invoice date
ot_data_final = online_transaction_clean.copy()
ot_data_final['invoice_date'] = pd.to_datetime(ot_data_final['invoice_date'])

# load data to s3
s3_bucket = "waia-data-dump"
# aws_s3_bucket = os.getenv('aws_s3_bucket')

# Write the transformed data to S3
key = "online_transactions_transformation/final/FCM_online_transactions.csv"
df_to_s3(ot_data_final, key, s3_bucket, aws_access_key_id, aws_secret_access_key)

# terminal run the below
# docker image build -t etl .
# docker run etl
# docker run --env-file .env etl
