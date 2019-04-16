#! /usr/bin/env python

import paramiko
import time
from pass_generator import genpass

ip_address = "192.168.0.1" 
username = "admin"
password = "admin1234"
new_pw = genpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
ssh_client.connect(ip_address,22,username,password,look_for_keys=False,allow_agent=False)

remote_connection = ssh_client.invoke_shell()
output = remote_connection.recv(65535)
print (output)

time.sleep(0.5)

remote_connection.send("conf t\n")
output = remote_connection.recv(65535)
print (output)

#remote_connection.send('username ' + username + ' privilege 15 password 0 ' + new_pw + '\n')
#remote_connection.send('end\n')
#remote_connection.send('wr mem\n')

time.sleep(1)

ssh_client.close

#ssh_client = paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
#ssh_client.connect(ip_address,22,username,new_pw)

#print(ssh_client.connect)

#ssh_client.close