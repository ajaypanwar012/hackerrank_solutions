#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
l=[]
def alternatingCharacters(s):
	c=0
	for i in range(1,len(s)):
		if s[i]==s[i-1]:
			c+=1
	l.append(c)

q = int(input())

for q_itr in range(q):
    s = input()
    alternatingCharacters(s)
for i in l:
	print(i)
