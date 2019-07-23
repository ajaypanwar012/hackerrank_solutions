#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
	l = list(set(s))
	for i in l:
		for j in range(len(s)-1):
			if i ==s[j] and i ==s[j+1]:
				sn=s.replace(s[j],'')
	print(sn)

l = int(input().strip())
s = input()

result = alternate(s)