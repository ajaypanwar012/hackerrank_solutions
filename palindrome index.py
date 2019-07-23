#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
l=[]
def palindromeIndex(s):
	i=0
	ind=-1
	while (i<len(s)//2):
		if s[i]!=s[-(i+1)]:
			if s[i+1]==s[-(i+1)]:
				ind = i
				break
			else:
				ind = len(s)-(i+1)
				break
		i+=1
	l.append(ind)

q = int(input())

for q_itr in range(q):
    s = input()

    palindromeIndex(s)

for i in l:
	print(i)
