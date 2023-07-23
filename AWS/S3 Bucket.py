# To create an S3 Bucket Using Python (Boto3)
# pip install boto3

import boto3

def create_s3_bucket(bucket_name, region='us-east-1'):
                                                                  # Replace these values with AWS credentials
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
    aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'
    
                                                                 # Create an S3 client using AWS credentials
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

                                                                 # Create S3 bucket
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
    except Exception as e:
        print(f"Failed to create S3 bucket: {e}")

if __name__ == "__main__":
    bucket_name = "your-unique-bucket-name"                      # Replace with your specific bucket name
    create_s3_bucket(bucket_name)


#Recheck
