#!/usr/bin/env python
# -*- coding: Utf-8 -*-

"""Import des modules pour le fonction du script"""
import subprocess #Permet l'ouverture d'un second script
import os
import sys
import csv #Permet la gestion des fichiers CSV
import datetime #Gestion du temps
import shutil #Gestion des fichiers dont la copie
from pass_generator import genpass #Génére le nouveau mot de passe

"""Définitions des fichiers CSV et du nouveau mot de passe"""
filename = "listing.csv" #Variable du listing du matériel
new_file = "suivi_listing/{0}_listing.csv".format(datetime.datetime.now()) #Variable du fichier temporaire du listing matériel
journal = "suivi/{0}_journal.csv".format(datetime.datetime.now()) #Variable du fichier journal
new_pw = genpass() #Variable du nouveau mot de passe

"""Fonction de lecture du listing réseau, de l'envoi des informations de connexions et d'écriture du nouveau listing"""
with open(filename, "r") as listing: #Lecture du listing matériel
    csv_reader = csv.DictReader(listing) #Transformation du listing en dictionnaire
    with open(new_file, "w") as new_listing: #Ecriture du fichier temporaire
            fieldnames = ["server", "ip", "user", "pw_user", "pw_suser", "old_pw"] #Définition des entêtes du dictionnaire
            csv_writer = csv.DictWriter(new_listing, fieldnames=fieldnames)
            csv_writer.writeheader()
            for line in csv_reader:  #Boucle de lecture de toutes lignes du listing
                script_to_use = "pass_{0}_change.py".format(line["server"]) #Variable du script de modification à ouvrir
                argv = [line["ip"],line["user"],line["pw_user"],new_pw,journal,line["pw_suser"]] #Liste des arguments à transférer au script
                ret = subprocess.run(["python3", script_to_use] + argv) #Ouverture du script, défition du lecteur, script à lancer + arguments
                if ret.returncode == 0: #Condition en fonction du retour du script, 0 : modifications effectuées
                    csv_writer.writerow({
                        "server": line["server"],
                        "ip": line["ip"],
                        "user": line["user"],
                        "pw_user": new_pw, 
                        "pw_suser": line["pw_suser"],
                        "old_pw": line["pw_user"],
                    })
                else: #autre que 0 : ligne réécrite à l'identique
                    csv_writer.writerow({
                        "server": line["server"],
                        "ip": line["ip"],
                        "user": line["user"],
                        "pw_user": line["pw_user"], 
                        "pw_suser": line["pw_suser"],
                        "old_pw": line["old_pw"],
                    })
    shutil.copy(new_file, filename) #Remplacement de l'ancien listing par le nouveau