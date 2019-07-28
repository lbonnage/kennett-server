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
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


##
# Endpoint for loading the website homepage
##
@app.route("/")
def loadIndex():
	return render_template('index.html')


##
# Receives the request to initialize the server.
# If the password is correct and the server isn't running, starts the server.
# If the password is correct and the server is running, returns the IP address.
# If the password is incorrect, returns a fail message to the browser.
##
@app.route('/initserver', methods=['POST'])
def init_server():

	inputted_password = request.form['password']

	return_data = {}

	message = 'Password Incorrect'

	if inputted_password == Config.SERVER_PASSWORD:

		#Instantiate the EC2 Server here
		client = boto3.client(
			'ec2',
			aws_access_key_id=Config.ACCESS_KEY,
			aws_secret_access_key=Config.SECRET_KEY,
			region_name=Config.EC2_REGION
		)		

		# ipaddress = manageServer(client)

	ipaddress = 'fake'
	print("Successfully started EC2 server with IP: " + ipaddress)
	return render_template('index.html', ipMessage=ipaddress)