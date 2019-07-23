#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
l=[]
def anagram(s):
	c1=0
	c2=0
	if len(s)%2!=0:
		l.append(-1)
	else:s="gcc"
		s1=s[:len(s)//2]
		s2=s[len(s)//2:]
		for i in range(len(s)//2):
			if s1[i] not in s2:
				c1+=1
			if s2[i] not in s1:
				c2+=1
		l.append(max(c2,c1))


q = int(input())

for q_itr in range(q):
    s = input()

    anagram(s)
for i in l:
	print(i)