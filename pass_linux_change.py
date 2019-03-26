#! /usr/bin/env python

import paramiko
import time

ip_address = "192.168.0.254" 
username = "admin"
password = "admin1234"
password_root = "root1234"
new_pw = "test1234"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successfuly connected to",  ip_address)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("su\n")
time.sleep(2)
remote_connection.send((password_root) + "\n")
time.sleep(2)
remote_connection.send("echo " + (username) + ":" + (new_pw) + " | chpasswd\n")
time.sleep(2)
remote_connection.send("exit\n")

output = remote_connection.recv(65535)
print (output)

ssh_client.close