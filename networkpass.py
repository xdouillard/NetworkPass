#!/usr/bin/env python

import paramiko     # Implementation of the SSHv2 protocol
import socket           
import getpass        # Gestion du mot de passe
import sys                 # Donne l'accès à certaines variables

""" Création de la fonction input_password """
def input_passwd():

    mesg = "Password: "
    old = getpass.getpass("Current %s" % mesg)
    new = getpass.getpass("New %s" % mesg)
    re_new = getpass.getpass("Retype New %s" % mesg)

    if new != re_new:
        print ("New RandomString does not match.")
        exit(1)

    return old, new

""" Création de la fonction main """
def main(argv):
    if len(argv) < 2:
        print ("USAGE : %s [srvlist.txt]" % argv[0])
        exit(1)

    srvlist_file = argv[1]

    old_password, new_password = input_passwd()
    print (new_password)

    srvlist = open(srvlist_file, 'r')
    lines = srvlist.readlines()

    for line in lines:

        line_sep = line.split()
        ip = line_sep[0]
        userlist = line_sep[1].split('/')
        for user in userlist:

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip, username='root', password='%s' % (old_password), timeout=5)

            except paramiko.ssh_exception.AuthenticationException:
                result = "Authentication failed"
            except socket.error:
                result = "Socket error"
            else:
                ssh.exec_command('echo "%s:%s" | chpasswd' % (user, new_password))
                result = "OK!"

            print "%s %s : %s " % (ip, user, result)

if __name__ == '__main__':
    main(sys.argv)