#! /usr/bin/env python

import paramiko
import time

ip_address = "192.168.2.2" 
username = "admin"
password = "test1234"
new_pw = "admin1234"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successfuly connected to"),  ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("username " + (username) + " privilege 15 password 0 " + (new_pw) + "\n")
remote_connection.send("end\n")
remote_connection.send("wr mem\n")

time.sleep(1)

ssh_client.close