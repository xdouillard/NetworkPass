#!/usr/bin/env python
# -*- coding: Utf-8 -*-
"""Script de génération de mot de passe"""

import secrets

def genpass():
    """Définis la longueur et la structure du mot de passe"""
    #Définition des caractères utilisables pour le mots de passe
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    special_char = "@#$%*=+-"

    #Variables du mot de passe
    password = ''
    count = 0
    length = 12
    upper_req = 4
    lower_req = 4
    num_req = 4
    special_req = 4

    #Génération du mot de passe
    while count < length:
        if (upper_req > 0) and (count < length):
            password += secrets.choice(uppercase)
            count += 1

        if (lower_req > 0) and (count < length):
            password += secrets.choice(lowercase)
            count += 1

        if (num_req > 0) and (count < length):
            password += secrets.choice(nums)
            count += 1

        if (special_req > 0) and (count < length):
            password += secrets.choice(special_char)
            count += 1

    #Edition du mot de passe
    return password
