#! /usr/bin/env python

import paramiko
import time

ip_address = "192.168.1.1" 
username = "xavier"
password = "test1234"
root_password = "root1234"
new_pw = "admin1234"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successfuly connected to"),  ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("su\n")
remote_connection.send((root_password) + "\n")
remote_connection.send("passwd" + (username) + "\n")
remote_connection.send((new_pw) + "\n")
remote_connection.send((new_pw) + "\n")

time.sleep(1)

ssh_client.close