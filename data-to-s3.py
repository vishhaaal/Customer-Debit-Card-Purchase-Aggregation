import os
import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')

def move_to_s3(bucket_name,data_folder):
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root,file)
                data_partition = 
