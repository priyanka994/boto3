import boto3
root=boto3.session.Session()
ec2 = root.client('ec2')
responce=ec2.describe_instances()
print(responce)
print("EC2 instance Describe", list(responce.keys()))


count=1
for res in responce.keys():
    print(res,": ",ec2.describe_instances()[res],"\n")
responce=ec2.describe_instances()["Reservations"]
for each_item in responce:
    print(list(each_item.keys()))
    for i in list(each_item.keys()):
        print(i+" "+str(each_item[i]))

    print("\nInstance Info \n")
    for each_instance_info in each_item["Instances"]:
        print(count,"\n")
        count=count+1
        print(each_instance_info["InstanceId"])
        print(each_instance_info["State"])

        #for attribute in each_instance_info.keys():
            #print(attribute,": ",each_instance_info[attribute])
