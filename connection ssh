#! /usr/bin/env python

import paramiko
import time

ip_address = "192.168.0.254"
username = "root"
password = "root1234"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print "Successfuly connected to", ip_address

ssh_client.close()