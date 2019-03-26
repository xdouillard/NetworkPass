#!/usr/bin/python
import sys
import secrets

#Définition des caractères utilisables pour le mots de passe
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
special_char = "!@#$%^&*()=+-~/[]{};:<>`"

#Variables du mot de passe
password = ''
count = 0
length = 12
upper_req = 4
lower_req = 4
num_req = 4
special_req = 4

#Génération du password
while (count < length):
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

#Edition du password
print ("PASSWORD: %s" % password)
