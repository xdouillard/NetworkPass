#! /usr/bin/env python
# -*- coding: Utf-8 -*-

import paramiko
import time
import sys
import csv
import socket

ip_address = sys.argv[1] 
username = sys.argv[2]
password = sys.argv[3]
new_pw = sys.argv[4]
journal = sys.argv[5]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
try:
    ssh_client.connect(ip_address, 22, username, password, look_for_keys=False, allow_agent=False)
except paramiko.AuthenticationException:
    result = "Authentication failed"
    with open(journal, "a") as suivi:
        csv_writer = csv.writer(suivi)
        csv_writer.writerow([ip_address,result])
    sys.exit(1)
except socket.error:
    result = "Socket error"
    with open("journal.csv", "a") as suivi:
        csv_writer = csv.writer(suivi)
        csv_writer.writerow([ip_address,result])
    sys.exit(2)
else:
    remote_connection = ssh_client.invoke_shell()
    result = "Authentication succeeded"
    remote_connection.send("conf t\n")
    remote_connection.send("username {0} privilege 15 password 0 {1}\n".format(username,new_pw))
    final = "Le mot de passe de la machine {1} a bien été changé : {0}".format(new_pw,ip_address)
    remote_connection.send("wr mem\n")
    remote_connection.send("exit\n")
with open("journal.csv", "a") as suivi:
    csv_writer = csv.writer(suivi)
    csv_writer.writerow([ip_address,result,final])
ssh_client.close
sys.exit(0)