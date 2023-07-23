import boto3
import os

def lambda_handler(event, context):
                                                                    # Replace these values with your actual source and backup bucket names
    source_bucket = 'your-source-bucket'
    backup_bucket = 'your-backup-bucket'

    s3_client = boto3.client('s3')

    try:
                                                                   # List all objects in the source bucket
        response = s3_client.list_objects_v2(Bucket=source_bucket)

        if 'Contents' in response:
            for obj in response['Contents']:
                                                                  # Copy each object from the source bucket to the backup bucket
                s3_client.copy_object(
                    Bucket=backup_bucket,
                    CopySource={'Bucket': source_bucket, 'Key': obj['Key']},
                    Key=obj['Key']
                )

        return {
            'statusCode': 200,
            'body': 'Backup process completed successfully.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error during backup process: {str(e)}'
        }
