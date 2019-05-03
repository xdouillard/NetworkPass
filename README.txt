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
    
Contributing
1 - Fork it
2 - Create your feature branch (git checkout -b my-new-feature)
3 - Commit your changes (git commit -am 'Add some feature')
4 - Push to the branch (git push origin my-new-feature)
5 - Create new Pull Request
