import os
import boto3

s3 = boto3.client('s3')

def move_to_s3(bucket_name, data_folder):
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                date_partition = file.split('_')[1].split('.')[0]
                s3_key = f"raw_data/date={date_partition}/{file}"
                s3.upload_file(file_path, bucket_name, s3_key)
                print(f"Uploaded {file} to S3 bucket {bucket_name} with partition {date_partition}")

def main():
    bucket_name = "s3-datalake-gds-storage"
    data_folder = r'C:\Users\Amisha\Customer-Debit-Card-Purchase-Aggregation\transaction_data'

    move_to_s3(bucket_name, data_folder)

if __name__ == "__main__":
    main()


