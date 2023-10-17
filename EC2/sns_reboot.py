import boto3
client = boto3.client('ec2')
sns=boto3.client('sns')
topic="arn:aws:sns:us-east-1:012405378730:reboot_ec2_instance"
id="i-09868ba36db050c5e"
try:
    response = client.reboot_instances(InstanceIds=[id,], DryRun=False)
    print(response)
    if (response['ResponseMetadata']['HTTPStatusCode']==200):
        print("reboot successfull")
        response = sns.publish(TopicArn=topic,Message='Reboot Sucess',Subject='Reboot Success')
        print("SNS Response",response)
    else:
        print("Reboot failed")
        response = sns.publish(TopicArn=topic,Message='Reboot Failed',Subject='Reboot Failed')
        print("SNS Response",response)
except Exception as e:
    print(e)