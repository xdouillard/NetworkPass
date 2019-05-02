#! /usr/bin/env python
# -*- coding: Utf-8 -*-

import subprocess
import os



proc = subprocess.Popen("test.py","192.168.0.1")
proc.wait()


#ouverture d'un fichier devnull du paquet os en écriture
#with open(os.devnull, 'w') as devnull:
    #execution du process et renvoi des infos vers devnull
#    ret = subprocess.run(["ls", "-l"],stdout=devnull)
#    print(ret.returncode)

#with open(os.devnull, 'w') as devnull:
    #execution du process et renvoi des infos vers devnull
    #ret = subprocess.run(["python3","test.py"],stdout=devnull)
    #print(ret.returncode)

#if ret.returncode == 1:
    #print("KO")
#else:
    #print("OK")