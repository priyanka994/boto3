import boto3

# Initialize the EC2 resource
ec2_resource = boto3.resource('ec2') 

# Define the parameters for your new instance
instance_params = {
    'ImageId': 'ami-041feb57c611358bd',  
    'InstanceType': 't2.micro',         
    'KeyName': 'new_keypair',         
    'MinCount': 1,
    'MaxCount': 2 
}

# Launch the instance
new_instance = ec2_resource.create_instances(**instance_params)[0]

# Wait for the instance to be running
new_instance.wait_until_running()

# Reload the instance to get the latest information
new_instance.reload()

# Get the instance ID
instance_id = new_instance.id

print(f'Instance {instance_id} created successfully.')
