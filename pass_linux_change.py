#! /usr/bin/env python
# -*- coding: Utf-8 -*-

import paramiko
import socket
import sys
import time
import pass_generator

print(sys.argv)

#Ordonner les arguments et mettre en place
ip_address = sys.argv[1] 
username = sys.argv[2]
password = sys.argv[3]
new_pw = sys.argv[4]
pw_root = sys.argv[5]

print(ip_address,username,password,new_pw,pw_root)

"""ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
try:
    ssh_client.connect(ip_address, 22, username, password, look_for_keys=False, allow_agent=False)
except paramiko.AuthenticationException:
    result = "Authentication failed"
    print(result)
    sys.exit(1)
except socket.error:
    result = "Socket error"
    print(result)
    sys.exit(1)
else:
    remote_connection = ssh_client.invoke_shell()
    result = "Authentication succeeded"
    print (result)
    if username != "root":
        remote_connection.send("su\n")
        time.sleep(0.5)
        remote_connection.send((pw_root) + "\n")
        time.sleep(0.5)
    else:
        remote_connection.send("echo {0}:{1} | chpasswd\n".format(username,new_pw))
        time.sleep(0.5)
        final = "Le mot de passe de la machine {1} a bien été changé : {0}".format(new_pw,ip_address)
        print(final)
        remote_connection.send("exit\n")

time.sleep(1)

ssh_client.close"""

