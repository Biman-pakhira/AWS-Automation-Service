import boto3
import os

print('* ' * 50)
print('AWS CLOUD AUTOMATION')
print('* ' * 50)

print('''ENTER 1 FOR AUTOMATING EC2
ENTER 2 FOR AUTOMATING S3
ENTER 3 FOR AUTOMATING IAM
ENTER 4 FOR AUTOMATING SECURITY GROUPS''')

n = int(input("\nENTER YOUR CHOICE: "))

try:
    if n == 1:
        def create_instance(Ami_id, Instance_type, Key_name, Security_group_ids):
            # Implement your instance creation logic here
            pass

        def start_instance(instance_id):
            # Implement your instance start logic here
            pass

        def describe_instance(instance_id):
            # Implement your instance description logic here
            pass

        def stop_instance(instance_id):
            # Implement your instance stop logic here
            pass

        def terminate_instance(instance_id):
            # Implement your instance termination logic here
            pass

        def main():
            # Create an EC2 instance
            Id = input("ENTER AMI ID: ")
            Kn = input("ENTER KEY NAME: ")
            Sg = input("ENTER SECURITY GROUP: ")

            Instance_id = create_instance(
                Ami_id=Id,
                Instance_type='t2.micro',
                Key_name=Kn,
                Security_group_ids=[Sg],
            )

            # Start the instance
            start_instance(Instance_id)

            # Describe the instance
            instance = describe_instance(Instance_id)

            # Print the instance details
            print('Instance ID: {}'.format(instance['InstanceId']))
            print('Instance State: {}'.format(instance['State']['Name']))
            print('Instance Public IP Address: {}'.format(instance['PublicIpAddress']))

            # Stop the instance
            stop_instance(Instance_id)

            # Terminate the instance
            terminate_instance(Instance_id)

        main()

    elif n == 2:
        ak = input("ENTER ACCESS KEY: ")
        sk = input("ENTER SECRET KEY: ")
        bn = input("ENTER BUCKET NAME: ")
        fp = input("ENTER FILE PATH: ")

        ACCESS_KEY_ID = os.environ[ak]
        SECRET_ACCESS_KEY = os.environ[sk]
        BUCKET_NAME = bn
        FILE_PATH = fp

        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY,
        )

        s3 = session.client('s3')
        s3.upload_file(FILE_PATH, BUCKET_NAME, os.path.basename(FILE_PATH))
        session.close()

    elif n == 3:
        # Create a client object for the IAM service
        iam = boto3.client('iam')

        # Create a new user
        user_name = input("ENTER USER NAME: ")
        response = iam.create_user(UserName=user_name)

        # Get the user's ARN
        user_arn = response['User']['Arn']

        # Attach the AdministratorAccess policy to the user
        pa = input("ENTER POLICY ARN: ")
        iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=pa,
        )

        # Print the user's ARN
        print(user_arn)

    elif n == 4:
        client = boto3.client('ec2')
        sgname = input("ENTER SECURITY GROUP NAME: ")
        sgdesc = input("ENTER SECURITY GROUP DESCRIPTION: ")

        # Create a security group
        security_group_name = sgname
        security_group_description = sgdesc

        response = client.create_security_group(
            GroupName=security_group_name,
            Description=security_group_description
        )

        # Get the security group ID
        security_group_id = response['GroupId']

        # Add an ingress rule to the security group
        ingress_rule_protocol = 'tcp'
        ingress_rule_port = 22
        ingress_rule_cidr_ip = '0.0.0.0/0'

        response = client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpProtocol=ingress_rule_protocol,
            FromPort=ingress_rule_port,
            ToPort=ingress_rule_port,
            CidrIp=ingress_rule_cidr_ip
        )

        # Print the security group details
        print(f'Security group name: {security_group_name}')
        print(f'Security group ID: {security_group_id}')
        print(f'Security group description: {security_group_description}')

    else:
        print("ENTER VALID INPUT")

except Exception as e:
    print("Error:", e)
    print("Program terminated!")
