import sys
import os
import boto3
sys.path.append(os.path.dirname(os.path.abspath("configuration.py")))
from configuration import Config

client = boto3.resource(
		'ec2',
		aws_access_key_id=Config.ACCESS_KEY,
		aws_secret_access_key=Config.SECRET_KEY,
		region_name=Config.EC2_REGION
	)

##
# Create an on-demand EC2 instance (more expensive, more reliable)
##
def create_on_demand():
	response = client.create_instances(
		ImageId = Config.EC2_AMIS[0],
		InstanceType = Config.EC2_INSTANCETYPE, 
		KeyName = Config.EC2_KEYPAIR,
		MaxCount = 1,
		MinCount = 1,
		SecurityGroups = Config.EC2_SECGROUPS)

	print ("[CreateOnDemand] On-demand EC2 Instance created.  Id: " + response[0].id)

##
# Create a spot EC2 instance (MUCH cheaper, less reliable)
# This won't work as easily, as you can't stop a Spot instance, only terminate, which means your data will be lost
##
def create_spot():
	response = client.create_instances(
		ImageId = Config.EC2_AMIS[0],
		InstanceType = Config.EC2_INSTANCETYPE, 
		KeyName = Config.EC2_KEYPAIR,
		MaxCount = 1,
		MinCount = 1,
		SecurityGroups = Config.EC2_SECGROUPS,
		InstanceMarketOptions = {
			'MarketType': 'spot',
			'SpotOptions': {
				'SpotInstanceType': 'one-time',
			}
		})


	print ("[CreateSpot] Spot EC2 Instance created.  Id: " + response[0].id)

# create_on_demand()