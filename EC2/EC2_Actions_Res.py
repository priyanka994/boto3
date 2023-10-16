import boto3

# Initialize the EC2 resource
ec2_resource = boto3.resource('ec2', region_name='us-east-1')  

# Define the instance ID
instance_id = 'i-065f8e21da6d2317f'  

# Get the instance
instance = ec2_resource.Instance(instance_id)

# Start the instance
#instance.start()

# Stop the instance
instance.stop()

"""# Reboot the instance
instance.reboot()

# Terminate the instance
instance.terminate()"""
