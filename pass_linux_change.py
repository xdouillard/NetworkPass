#! /usr/bin/env python

import paramiko
import time
import pass_generator

#Ordonner les arguments et mettre en place
ip_address = "192.168.0.254" 
username = "root"
password = "root1234"
password_root = "root1234"

moto = "echo {0}:{1} | chpasswd\n".format(username,pass_generator.genpass())

print(moto)



#ssh_client = paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
#ssh_client.connect(ip_address, 22, username, password, look_for_keys=False, allow_agent=False)

#print ("Successfuly connected to",  ip_address)

#remote_connection = ssh_client.invoke_shell()
 
#if username != "root":
#    remote_connection.send("su\n")
#    time.sleep(1)
#    remote_connection.send((password_root) + "\n")
#    time.sleep(1)
#else:
#    remote_connection.send("echo {0}:{1} | chpasswd\n".format(username, new_pw))
#    time.sleep(1)
#    remote_connection.send("exit\n")

#time.sleep(1)

#ssh_client.close

#ssh_client = paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
#ssh_client.connect(hostname=ip_address,username=username,password=new_pw) #Trouver que trenvoi ssh_connect 0,1,true,false...

#print("Le mot de passe à bien été changé sur la machine",  ip_address)