"""
this is a script to take a backup feom local to aws s3
boto-> used to do AWS tasks using python
"""
import boto3

# Create an S3 resource
s3 = boto3.resource("s3")

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region):
    # Create a bucket with proper keyword arguments
    s3.create_bucket(
        Bucket=bucket_name,  # Bucket name as a keyword argument
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("Bucket created successfully")

def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(key=key_name,Body=data)
    print("Backup uploaded successfully")
    

bucket_name = "python-practice"
region = "us-west-2"

# Create a new S3 bucket
#create_bucket(s3, bucket_name, region)

# Display all S3 buckets
#show_bucket(s3)
file_name = r"D:\python-prac\backups"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")
