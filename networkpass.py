#!/usr/bin/env python
# -*- coding: Utf-8 -*-

"""Script principal"""
import subprocess #Permet l'ouverture d'un second script
import csv #Permet la gestion des fichiers CSV
import datetime #Gestion du temps
import shutil #Gestion des fichiers dont la copie
from pass_generator import genpass #Génére le nouveau mot de passe

#Variable du listing du matériel
FILENAME = "listing.csv"
#Variable du fichier temporaire du listing matériel
NEW_FILE = "suivi_listing/{0}_listing.csv".format(datetime.datetime.now())
#Variable du fichier journal
JOURNAL = "suivi/{0}_journal.csv".format(datetime.datetime.now())
#Variable du nouveau mot de passe
NEW_PW = genpass()

#Lecture du LISTING matériel
with open(FILENAME, "r") as LISTING:
    #Transformation du LISTING en dictionnaire
    CSV_READER = csv.DictReader(LISTING)
    #Ecriture du fichier temporaire
    with open(NEW_FILE, "w") as NEW_LISTING:
        #Définition des entêtes du dictionnaire
        FIELDNAMES = ["server", "ip", "user", "pw_user", "pw_suser", "old_pw"]
        CSV_WRITER = csv.DictWriter(NEW_LISTING, fieldnames=FIELDNAMES)
        CSV_WRITER.writeheader()
        #Boucle de lecture de toutes lignes du listing
        for line in CSV_READER:
            #Variable du script de modification à ouvrir
            SCRIPT_TO_USE = "pass_{0}_change.py".format(line["server"])
            #Liste des arguments à transférer au script
            ARGV = [line["ip"], line["user"], line["pw_user"], NEW_PW, JOURNAL, line["pw_suser"]]
            #Ouverture du script, défition du lecteur, script à lancer + arguments
            ret = subprocess.run(["python3", SCRIPT_TO_USE] + ARGV)
            #Condition en fonction du retour du script, 0 : modifications effectuées
            if ret.returncode == 0:
                CSV_WRITER.writerow({
                    "server": line["server"],
                    "ip": line["ip"],
                    "user": line["user"],
                    "pw_user": NEW_PW,
                    "pw_suser": line["pw_suser"],
                    "old_pw": line["pw_user"],
                })
            #autre que 0 : ligne réécrite à l'identique
            else:
                CSV_WRITER.writerow({
                    "server": line["server"],
                    "ip": line["ip"],
                    "user": line["user"],
                    "pw_user": line["pw_user"],
                    "pw_suser": line["pw_suser"],
                    "old_pw": line["old_pw"],
                })
#Remplacement de l'ancien LISTING par le nouveau
shutil.copy(NEW_FILE, FILENAME)
