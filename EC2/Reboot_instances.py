import boto3
instance_id="i-09868ba36db050c5e"
ec2=boto3.client("ec2")
responce = ec2.reboot_instances(InstanceIds=[instance_id])
print(responce)
