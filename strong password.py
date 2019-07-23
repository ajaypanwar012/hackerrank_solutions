#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"

	x = 6-len(password)
	n=True
	l=True
	u=True
	s=True
	c=0
	for i in password:
		if i in numbers and n:
			c+=1
			n=False
		elif i in lower_case and l:
			c+=1
			l=False
		elif i in upper_case and u:
			c+=1
			u=False
		elif i in special_characters and s:
			c+=1
			s=False
		else:
			pass

	if len(password) >= 6:
		return (4-c)
	elif x>(4-c):
		return x
	else:
		return (4-c)



n = int(input())

password = input()

print(minimumNumber(n, password))
