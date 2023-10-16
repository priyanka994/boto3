import boto3
root=boto3.session.Session()
ec2 = root.client('ec2')

instance_params = {
    'ImageId': 'ami-053b0d53c279acc90',  
    'InstanceType': 't2.micro',         
    'KeyName': 'new_keypair',         
    'MinCount': 1,
    'MaxCount': 3     
}

# Launch the instance
response = ec2.run_instances(**instance_params)

# Get the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

print(f'Instance {instance_id} created successfully.')