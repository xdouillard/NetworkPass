#!/usr/bin/python
import sys
import secrets

#Defines all possible characters for the password
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
special_char = "!@#$%^&*()=+-~/[]{};:<>`"

#Changes input to an integer value
length = 12
upper_req = 4
lower_req = 4
num_req = 4
special_req = 4

#Determines if there was an error. If there wasn't, then the password is generated
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

#Displays the password
print ("PASSWORD: %s" % password)
