import boto3
import time 

# Initialize the S3 client
s3 = boto3.client('s3', region_name='us-east-1')  # Replace 'us-east-1' with your desired region

# Define a unique bucket name
bucket_name = 'bucket6747657' 

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name)

print(f'S3 bucket {bucket_name} created successfully.')

# Define the local file path and the S3 object key (name in the bucket)
local_file_path = 'C:/Users/Dell/Desktop/Praticals/Youtube_classes/S3_Boto3/S3_Bucket_res.py'
s3_object_key = 'S3_Bucket_res.py' 

# Upload the file
s3.upload_file(local_file_path, bucket_name, s3_object_key)

print(f'File uploaded successfully to {bucket_name}/{s3_object_key}')
local_file_path = 'C:/Users/Dell/Desktop/Praticals/Youtube_classes/S3_Boto3/S3_Bucket_res3.py'
s3.download_file(bucket_name, s3_object_key, local_file_path)

print(f'File downloaded successfully to {local_file_path}')

s3.delete_object(Bucket=bucket_name, Key=s3_object_key)