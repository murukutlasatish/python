import boto3
import json
def get_ec2_instance_details(instance_id, region):
    # this statement will create EC2 client
    ec2_client = boto3.client('ec2', region_name=region)
    # this will Describe the EC2 instance
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    # this will Extract instance details
    instance = response['Reservations'][0]['Instances'][0]
    # Prepare instance details for JSON output
    instance_details = {
        "Instance ID": instance['InstanceId'],
        "Instance Type": instance['InstanceType'],
        "State": instance['State']['Name'],
        "Private IP": instance.get('PrivateIpAddress', 'N/A'),
        "Public IP": instance.get('PublicIpAddress', 'N/A'),
        "Launch Time": str(instance['LaunchTime']),  
        "Tags": instance.get('Tags', [])
    }
    # Return the instance details as a JSON string with indent 4
    return json.dumps(instance_details, indent=4)

if _name_ == "_main_":
    instance_id = "i-071a4a0b58177eba2"  
    region = "us-west-2"  
    instance_json = get_ec2_instance_details(instance_id, region)
    print(instance_json)
