#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
	i=1
	flag=0
	while i<=(len(s)):
		if s[i]-s[i-1]==1:
			i+=1
			flag=1
		elif s[i+1:i+3]

q = int(input())

for q_itr in range(q):
    s = input()

    separateNumbers(s)
