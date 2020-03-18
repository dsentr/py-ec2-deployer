#!/usr/bin/env python3

import yaml
import boto3
from botocore.exceptions import ClientError, ParamValidationError

def parse_yml(deploy_config):
    with open(deploy_config, 'r') as file:
        # Deserailize yaml file into python dictionary
        doc = yaml.load(file, Loader=yaml.FullLoader)

    # Create kwarg arguments for ec2.create_instances
    inputs={}
    for x, y in doc['instance'].items():
        appenditem={x : y}
        inputs.update(appenditem)
    
    # Safety feature so no more than 5 instances are deployed at once
    if (inputs["MaxCount"] > 5):
        inputs["MaxCount"] = 5 
    return inputs

def main():
    args=parse_yml("deployment.yml")
    # Start of AWS SDK for Python (boto3) usage
    # Change below variables to proper region and aws profiles on local machine
    AWS_PROFILE='dev'
    AWS_REGION='us-east-1'
    boto3.setup_default_session(profile_name=AWS_PROFILE,region_name=AWS_REGION)

    try:
        ec2 = boto3.resource('ec2')
        instance = ec2.create_instances(**args)
        # old style string formatting for positional formatting.
        print ("InstanceID is: %s" %(instance[0].id))
        print ("Private IP Address is: %s" %(instance[0].private_ip_address))
    except ClientError as e:
        print("Client Error: %s" %(e))
    except ParamValidationError as e:
        print("Parameter Validation Error: %s" %(e))


if __name__ == '__main__':
    main()