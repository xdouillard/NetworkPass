#! /usr/bin/env python
# -*- coding: Utf-8 -*-

"""Script de modification du mot de passe via SSH pour matériel LINUX"""
import socket #Gestion de la lecture des ports
import sys #Options système
import time #Mise en place de temporisation
import csv #Permet la gestion des fichiers CSV
import paramiko #Gestion de la connexion ssh

#Récupération des arguments du fichiers CSV envoyés par le script principal
IP_ADDRESS = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]
NEW_PW = sys.argv[4]
JOURNAL = sys.argv[5]
PW_ROOT = sys.argv[6]

#Connection SSH et modification du mot de passe
SSH_CLIENT = paramiko.SSHClient()
SSH_CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try: #Ouverture de la connection
    SSH_CLIENT.connect(IP_ADDRESS, 22, USERNAME, PASSWORD, look_for_keys=False, allow_agent=False)
#Gestion de l'erreur d'authentification
except paramiko.AuthenticationException:
    RESULT = "Authentication failed"
    with open(JOURNAL, "a") as suivi: #Ecriture dans le journal
        CSV_WRITER = csv.writer(suivi)
        CSV_WRITER.writerow([IP_ADDRESS, RESULT])
    sys.exit(1) #Renvoi de l'erreur 1
#Gestion de l'erreur de port (matériel non joignable)
except socket.error:
    RESULT = "Socket error"
    with open(JOURNAL, "a") as suivi: #Ecriture dans le journal
        CSV_WRITER = csv.writer(suivi)
        CSV_WRITER.writerow([IP_ADDRESS, RESULT])
    sys.exit(2) #Renvoi de l'erreur 2
#Connection réussi
else:
    REMOTE_CONNECTION = SSH_CLIENT.invoke_shell()
    RESULT = "Authentication succeeded"
    #Si l'utilisateur est différent de root
    if USERNAME != "root":
        REMOTE_CONNECTION.send("su\n")
        time.sleep(2)
        REMOTE_CONNECTION.send("{0}\n".format(PW_ROOT))
        time.sleep(2)
        #Modification du mot de passe
        REMOTE_CONNECTION.send("echo {0}:{1} | chpasswd\n".format(USERNAME, NEW_PW))
        time.sleep(1)
        #REMOTE_CONNECTION.send("history -c\n") #Supprime l'historique des commandes
        #time.sleep(0.5)
        #Variable validant le changement de mot de passe
        FINAL = "Le mot de passe du matériel {1} a bien été changé : {0}".format(NEW_PW, IP_ADDRESS)
        REMOTE_CONNECTION.send("exit\n")
    #Si l'utilisateur est root
    else:
        #Modification du mot de passe
        REMOTE_CONNECTION.send("echo {0}:{1} | chpasswd\n".format(USERNAME, NEW_PW))
        time.sleep(1)
        #REMOTE_CONNECTION.send("history -c\n") #Supprime l'historique des commandes
        #time.sleep(0.5)
        #Variable validant le changement de mot de passe
        FINAL = "Le mot de passe du matériel {1} a bien été changé : {0}".format(NEW_PW, IP_ADDRESS)
        REMOTE_CONNECTION.send("exit\n")
with open(JOURNAL, "a") as suivi: #Ecriture dans le journal
    CSV_WRITER = csv.writer(suivi)
    CSV_WRITER.writerow([IP_ADDRESS, RESULT, FINAL])
#Fermeture de la connection
#SSH_CLIENT.close
sys.exit(0)
