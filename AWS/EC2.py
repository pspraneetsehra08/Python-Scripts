# To Create an EC2 Instance using BOTO3
# pip install boto3

import boto3

def create_ec2_instance():
   
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'                        # Replace these values with AWS credentials and region (Check College Email)
    aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'
    region = 'us-east-1'                                             # Replace with your region
    
                                                                     # Create an EC2 client using AWS credentials
    ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

                                                                     # Specify the parameters for the instance
    instance_params = {
        'ImageId': 'ami-0c55b159cbfafe1f0',                          # Replace with the desired AMI ID
        'InstanceType': 't2.micro',                                  # Replace with the desired instance type
        'KeyName': 'your-key-pair-name',                             # Replace with your key pair name
        'MinCount': 1,
        'MaxCount': 1
    }

                                                                     # Launch the instance
    response = ec2.run_instances(**instance_params)

    if response['Instances']:
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instance created with ID: {instance_id}")
    else:
        print("Failed to create instance.")

if __name__ == "__main__":
    create_ec2_instance()
  
