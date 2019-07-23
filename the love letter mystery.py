#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
l=[]
def theLoveLetterMystery(s):
	c=0
	for i in range(len(s)//2):
		if s[i]==s[-(i+1)]:
			pass
		else:
			c+=abs(ord(s[i])-ord(s[-(i+1)]))
	l.append(c)


q = int(input())

for q_itr in range(q):
    s = input()
    theLoveLetterMystery(s)
for i in l:
	print(i)