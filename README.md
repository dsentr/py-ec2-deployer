# py-ec2-deployer

This script demonstrates using the AWS SDK Boto3 python library to deploy an EC2. The script takes yaml file of EC2 specifications to deploy an EC2 instance.



## Getting started

- clone this repository
- fill out the yaml file with the correct information such as Subnet ID and AMI.
- Start a new virtual environment named venv in this folder `python3 -m venv venv`
- Activate the new virtual environment `source venv/bin/activate`
- Install the required python packaged from requirements.txt `pip install -r requirements.txt` This was created using `pip freeze > requirements.txt`
- Run the script to deploy an EC2 `./main.py`


