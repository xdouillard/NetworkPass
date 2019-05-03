#! /usr/bin/env python
# -*- coding: Utf-8 -*-

"""Importation des modules nécessaires au fonctionnement du script"""
import paramiko #Gestion de la connection ssh
import socket #Gestion de la lecture des ports
import sys #Options système
import time #Mise en place de temporisation
import csv #Permet la gestion des fichiers CSV

"""Récupération des arguments du fichiers CSV envoyés par le script principal"""
ip_address = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
new_pw = sys.argv[4]
journal = sys.argv[5]

"""Connection SSH, gestion des erreurs et changement du mot de passe"""
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
try: #Ouverture de la connection
    ssh_client.connect(ip_address, 22, username, password, look_for_keys=False, allow_agent=False)
except paramiko.AuthenticationException: #Gestion de l'erreur d'authentification
    result = "Authentication failed"
    with open(journal, "a") as suivi: #Ecriture dans le journal
        csv_writer = csv.writer(suivi)
        csv_writer.writerow([ip_address,result])
    sys.exit(1) #Renvoi de l'erreur 1
except socket.error: #Gestion de l'erreur de port (matériel non joignable)
    result = "Socket error"
    with open(journal, "a") as suivi: #Ecriture dans le journal
        csv_writer = csv.writer(suivi)
        csv_writer.writerow([ip_address,result])
    sys.exit(2) #Renvoi de l'erreur 2
else: #Connection réussi
    remote_connection = ssh_client.invoke_shell()
    result = "Authentication succeeded"
    remote_connection.send("conf t\n") #Configuration routeur
    remote_connection.send("username {0} privilege 15 password {1}\n".format(username,new_pw)) #Modification du mot de passe
    final = "Le mot de passe de la machine {1} a bien été changé : {0}".format(new_pw,ip_address) #Variable validant le changement de mot de passe
    remote_connection.send("copy running-config startup-config\n") #Sauvegarde de la configuration routeur
    time.sleep(0.5)
    remote_connection.send("\n")
    remote_connection.send("exit\n") #Fin de la configuration routeur
with open(journal, "a") as suivi: #Ecriture dans le journal
    csv_writer = csv.writer(suivi)
    csv_writer.writerow([ip_address,result,final])
ssh_client.close #Fermeture de la connection
sys.exit(0) #Renvoi du bon déroulé du script