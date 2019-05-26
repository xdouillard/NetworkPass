# NetworkPass

Ce script a pour but la mise à jour automatique des mots de passe des différents éléments réseaux(Firewall, routeurs, switchs...)
Le script principal "Networkpass" fonctionne avec plusieurs sous script :
  - Genpass : générateur de mot de passe
  - pass_******_change : modifie le mot de passe en fonction du type de matériel, les * seront changées en cisco, linux, zyxel... En fonction de chaque type, il peut être créer un script de modification.

Le matériel réseau doit être répertorié dans un fichier CSV nommé "listing.csv".

En plus de la modification du mot de passe, le script génére deux fichiers CSV :
  - un fichier "date_heure_journal.csv", ce fichier sera créé dans un répertoire nommé "suivi"
    Il liste l'ensemble des matériels réseaux avec son retour de mise à jour, mise à jour réussie ou l'erreur pour laquelle la mise à jour du mot de passe n'a pu ce faire. 
  - un fichier "dat_heure_listing.csv", ce fichier sera crée dans un répertoire nommé "suivi listing"
    Il reprendra ligne par ligne le fichier "listing" pour être réécrit avec modification de mot de passe si la mise à jour à fonctionner ou à l'identique si la mise à jour n'a pas fonctionné
    En tout fin de mise à jour quand tous les matériels réseaux ont été passés en revu, ce fichier "dat_heure_listing.csv" remplace le fichier "listing.csv" dans le répertoire principal

Axe d'amélioration :
  - Ignorer une ligne dans le fichier listing.csv si celle-ci commence par #, mais l'écrire tout de même dans dans le fichier "dat_heure_listing.csv"
  - Amélioration générale du code, mise en place de Programmation Orienté Objet

This script is intended to automatically update the passwords of the different network elements (firewall, routers, switches ...)
The main script "Networkpass" works with several sub-scripts:
  - Genpass: password generator
  - pass _ ****** _ change: change the password according to the type of material, the * will be changed to cisco, linux, zyxel ... Depending on each type, it can be create a modification script.

The network hardware must be listed in a CSV file named "listing.csv".

In addition to changing the password, the script generates two CSV files:
  - a file "date_heure_journal.csv", this file will be created in a directory named "monitoring"
    It lists all the network hardware with its update, update successfully, or the error for which the password update was unable to do so.
  - a file "dat_heure_listing.csv", this file will be created in a directory named "follow listing"
    It will resume line by line the file "listing" to be rewritten with modification of password if the update to function or identically if the update did not work
    At the very end of the update when all network devices have been reviewed, this file "dat_heure_listing.csv" replaces the file "listing.csv" in the main directory

Area for improvement :
  - Ignore a line in the listing.csv file if it starts with #, but write it in the file "dat_heure_listing.csv"
  
Contributing
1 - Fork it
2 - Create your feature branch (git checkout -b my-new-feature)
3 - Commit your changes (git commit -am 'Add some feature')
4 - Push to the branch (git push origin my-new-feature)
5 - Create new Pull Request
