#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
	x=0
	c=0
	for i in b:
		if b[x:x+3]=="010":
			c+=1
			x+=3
		else:
			x+=1

#	if (len(b)%3)!=0:
#		if b[-3:]=="010":
#			c+=1
	print(c)

n = int(input())
b = input()

beautifulBinaryString(b)
