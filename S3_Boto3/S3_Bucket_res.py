import boto3

# Initialize the S3 resource
s3_resource = boto3.resource('s3', region_name='us-east-1')  # Replace 'us-east-1' with your desired region

# Define a unique bucket name
bucket_name = 'bucket-85784' 

# Create the S3 bucket
bucket = s3_resource.create_bucket(Bucket=bucket_name)

print(f'S3 bucket {bucket_name} created successfully.')

# Define the local file path and the S3 object key (name in the bucket)
local_file_path = 'C:/Users/Dell/Desktop/Praticals/Youtube_classes/S3_Boto3/S3_Bucket_res.py'
s3_object_key = 'S3_Bucket_res.py' 

bucket = s3_resource.Bucket(bucket_name)
bucket.upload_file(local_file_path, s3_object_key)

print(f'File uploaded successfully to {bucket_name}/{s3_object_key}')

local_file_path = 'C:/Users/Dell/Desktop/Praticals/Youtube_classes/S3_Boto3/S3_Bucket_res2.py'
bucket.download_file(s3_object_key, local_file_path)

print(f'File downloaded successfully to {local_file_path}')


s3_object = s3_resource.Object(bucket_name, s3_object_key)
# Delete an object
#s3_object.delete()

