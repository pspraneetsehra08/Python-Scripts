# S3 bucket creation script to include error handling, logging, and a more client-friendly interface.

import boto3
import logging

def create_s3_bucket(bucket_name, region='us-east-1'):
                                                                     # Create a logger to record events
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

                                                                     # Create a file handler to write log messages to a file
    log_file = 's3_bucket_creation.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

                                                                     # Create a formatter to format the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

                                                                     # Add the file handler to the logger
    logger.addHandler(file_handler)

    try:
                                                                     # Replace these values with your AWS credentials
        aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
        aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'

                                                                     # Create an S3 client using your AWS credentials
        s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

                                                                     # Create the S3 bucket
        response = s3.create_bucket(Bucket=bucket_name)

        logger.info(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
        print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
    except boto3.exceptions.S3CreateError as e:
        logger.error(f"Failed to create S3 bucket: {e}")
        print("Failed to create S3 bucket. Please ensure the bucket name is unique and follows S3 naming guidelines.")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        print("An unexpected error occurred. Please contact support for assistance.")

if __name__ == "__main__":
    bucket_name = "your-unique-bucket-name"                          # Replace with your desired bucket name
    create_s3_bucket(bucket_name)
