import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2') 

# Define the key pair name
key_pair_name = 'my_keypair_10'

# Create the key pair
response = ec2.create_key_pair(KeyName=key_pair_name)

# Save the private key to a file
with open(f'{key_pair_name}.ppk', 'w') as key_file:
    key_file.write(response['KeyMaterial'])

print(f'Key pair {key_pair_name} created successfully.')
