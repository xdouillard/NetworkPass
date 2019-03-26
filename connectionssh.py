#! /usr/bin/env python

import time
import paramiko

ip_address = "192.168.0.11"
username = "xavier"
password = "@dmin1234"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print ("Successfuly connected to"),  ip_address



# ssh_client.exec_command("su")


ssh_client.close()
