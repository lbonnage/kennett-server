from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from multiprocessing import Process
from configuration import Config
import json
import boto3
import time
import paramiko
import os

app = Flask(__name__)
CORS(app)

#Paraminko SSH information
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, Config.SSH_KEY_FILE_PATH)
key = paramiko.RSAKey.from_private_key_file(filename)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


##
# SSH into the server and execute the command to boot the Minecraft server
##
def init_server_commands(instance_ip, server):

	# Connect via SSH to the instance
	try:
		# Use 'ubuntu' as username and 'instance_ip' as the public IPv4 of the EC2 instance
		ssh_client.connect(hostname=instance_ip, username='ubuntu', pkey=key)

		# Create the correct path to the server jar using the selected server number
		jar_path = Config.SERVER_JAR_PATHS[int(server)]
		print('[Server] About to execute command with server jar_path: ' + jar_path)

		# Execute a Unix command via SSH after connecting to the instance
		stdin, stdout, stderr = ssh_client.exec_command("screen -dmS minecraft bash -c 'sudo java " + Config.MEMORY_ALLOCATION + "-jar " + server_path + "nogui'")
		print("[Server] Command executed")
		print('[Server] stdin: ' + stdin)
		print('[Server] stdout: ' + stdout)
		print('[Server] stderr: ' + stderr)

		# Close the SSH connection once the job is done
		ssh_client.close()

	except:
		print('[Server] An error has occurred while attempting to run commands through SSH')


##
# Waits for the server to reach a valid state so commands can be run
# Server is the string number of the dropdown choice representing the server that you want to launch.
##
def server_wait_ok(instance_ip, ec2_client, server):

	checks_passed = False
	status = 'initializing'
	instance_ids = [Config.INSTANCE_ID]

	while (not checks_passed) and (status == 'initializing'):
		status_check_response = ec2_client.describe_instance_status(InstanceIds = instance_ids)

		status = status_check_response['InstanceStatuses'][0]['InstanceStatus']['Status']

		checks_passed = status == 'ok'

		time.sleep(5)

	if checks_passed:
		init_server_commands(instance_ip, server)
	else:
		print('[Server] An error has occurred booting the server')


##
# Starts the desired EC2 instance from the inputted client
# Server is the string number of the dropdown choice representing the server that you want to launch.
##
def start_server(ec2_client, server):

	# Get the proper variables to attempt to start the desired EC2 instance and launch the Minecraft server
	return_string = 'ERROR'
	instance_ids = [Config.INSTANCE_ID]
	response = ec2_client.start_instances(InstanceIds = instance_ids)

	state_code = 0

	while not (state_code == 16):
		time.sleep(3)

		print('[Server] AWS EC2 Start Response:')
		print(str(response))
		print('\n')

		response = ec2_client.describe_instances(InstanceIds = instance_ids)
		reservation = response['Reservations'][0]
		instances = reservation['Instances']
		instance = instances[0]
		state_code = instance['State']['Code']

		print('[Server] Server instances:')
		print(instances)
		print('\n')

	ip_address = instance['PublicIpAddress']
	return_string = 'Server is starting, this may take a minute. IP Address: ' + ip_address

	p = Process(target=server_wait_ok, args=(ip_address, ec2_client, server))
	p.start()
	return return_string


##
# If the EC2 server is not running, starts the server and returns the IP address.
# Server input is a string representing the desired server to launch if there is none currently running.
##
def manage_server(ec2_client, server):
	return_string = 'ERROR'

	# Find the details of our specific EC2 instance within the EC2 client
	instance_ids = [Config.INSTANCE_ID]
	response = ec2_client.describe_instances(InstanceIds = instance_ids)
	reservation = response['Reservations'][0]

	instances = reservation['Instances']

	print('[Server] Server instances:')
	print(instances)
	print('\n')

	if len(instances) > 0:
		instance = instances[0]

		state = instance['State']
		state_name = state['Name']

		# The instance isn't running
		if (state_name == 'stopped') or (state_name == 'shutting down'):
			return_string = start_server(ec2_client, server)
		elif state_name == 'running':
			return_string = 'IP: ' + instance['PublicIpAddress']
		else:
			return_string = 'ERROR'

	return return_string


##
# Endpoint for loading the website homepage
##
@app.route("/")
def load_index():
	return render_template('index.html')


##
# Receives the request to initialize the server.
# If the password is correct and the server isn't running, starts the server.
# If the password is correct and the server is running, returns the IP address.
# If the password is incorrect, returns a fail message to the browser.
##
@app.route('/init_server', methods=['POST'])
def init_server():

	inputted_password = request.form['password']
	inputted_server = request.form['server']

	print("Server: " + inputted_server)

	return_data = {}

	message = '[Server] Password Incorrect'
	ip_address = 'Password incorrect'

	if inputted_server == '0':
		message = '[Server] Please choose a valid server'
		ip_address = 'Please choose a valid server'

	elif inputted_password == Config.SERVER_PASSWORD:

		# Instantiate the EC2 Server here or return the IP if it is already running
		ec2_client = boto3.client(
			'ec2',
			aws_access_key_id=Config.ACCESS_KEY,
			aws_secret_access_key=Config.SECRET_KEY,
			region_name=Config.EC2_REGION
		)		

		ip_address = manage_server(ec2_client, inputted_server)
		message = '[Server] Successfully started EC2 server with IP: ' + ip_address

	print(message)
	return render_template('index.html', ipMessage=ip_address)