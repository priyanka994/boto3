import boto3
root=boto3.session.Session()
ec2 = root.client('ec2')
# Start instance
#response = ec2.start_instances(InstanceIds=['i-02bb64af169629deb'])
# Stope Instance
response = ec2.stop_instances(InstanceIds=['i-0a0b84beb15fd35db'])
# Reboot instance
response = ec2.reboot_instances(InstanceIds=['i-02bb64af169629deb'])
# Terminate Instance
response = ec2.terminate_instances(InstanceIds=['i-02bb64af169629deb'])
