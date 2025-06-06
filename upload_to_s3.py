import os
from dotenv import load_dotenv
import boto3

# Load AWS credentials from .env
load_dotenv()

# Connect to S3
s3 = boto3.client("s3")

# Set file + destination
bucket_name = "gdpr-data-kaggle"
local_file_path = "full/path/to/gdpr_violations.csv" 
s3_key = "raw/gdpr/gdpr_violations.csv"

# Upload
try:
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f"✅ Uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("❌ Upload failed:", e)
