# On-Demand Minecraft Server for Kennett Group

Python Flask/AWS application, creates a website that can be used to launch an AWS EC2 instance to host a Minecraft server.  Users can request for the server to start through the webpage.  The server will shut down automatically after 15 minutes when there are no players, in order to reduce hosting costs.


## AWS Setup


## Web Application Deployment


## AWS Instance Configuration
1. Connect through SSH to the server using preferred client (Putty, MobaXTerm, etc.)
2. Make the ubuntu user admin if it isn't already with
`adduser ubuntu sudo`
3. Install Java JDK onto the instance.  Use
`sudo apt install openjdk-8-jdk-headless`.
You may need to run
`sudo apt-get update`
to update package list.
4. Using a FTP client (such as FileZilla) connect to the same address with the same username you used to connect to the SSH client.  Drag all the files from the `serverfiles` directory into the `/home/ubuntu` directory of the instance.
5. Download your desired Minecraft servers and rename the executable that you would normally run to start the server to `server.jar`.
6. Input the following to the SSH client **exactly**:
`sudo mkdir screens`
`mkdir servers`
Following this, create a directory in the `servers` directory for each type of server you are trying to be able to run using `mkdir servers/{servername}`.  Then, copy the server files into the corresponding directory using the FTP client.  Continue with the follow inputs.
`sudo chmod 777 servers`
`sudo chmod 700 /home/ubuntu`
`export SCREENDIR=/home/ubuntu/screens`
`crontab /home/ubuntu/crontab`
7. Following this, you can just restart.


## Goals
 - Choice of server to run
 - Current player count
 - If the server is already running it should tell you when you enter the password
 - Better security (maybe?)