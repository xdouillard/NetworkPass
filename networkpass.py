#!/usr/bin/env python
# -*- coding: Utf-8 -*-

"""Import des modules pour le fonction du script"""
import os
import sys
import csv
import datetime
import shutil
from pass_generator import genpass

"""Définitions des fichiers CSV"""
filename = "listing.csv"
new_file = "csv/{0}_listing.csv".format(datetime.datetime.now())

"""Fonction de lecture du listing réseau, de l'envoi des informations de connexions et d'écriture du nouveau listing"""
with open(filename, "r") as listing:
        csv_reader = csv.DictReader(listing)
        with open(new_file, "w") as new_listing:
                fieldnames = ["server", "ip", "user", "pw_user", "pw_suser", "old_pw"]
                csv_writer = csv.DictWriter(new_listing, fieldnames=fieldnames)
                csv_writer.writeheader()
                for line in csv_reader:
                        new_pw = genpass()
                        script_to_use = "python3 pass_{0}_change.py {1} {2} {3} {4} {5}".format(line["server"],line["ip"],line["user"],line["pw_user"],new_pw,line["pw_suser"])
                        os.system(script_to_use)
                        csv_writer.writerow({
                                "server": line["server"],
                                 "ip": line["ip"], 
                                 "user": line["user"], 
                                 "pw_user": new_pw, 
                                 "pw_suser": line["pw_suser"], 
                                 "old_pw": line["pw_user"],
                        })
        shutil.copy(new_file, filename)