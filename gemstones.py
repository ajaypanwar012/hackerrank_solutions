#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr,ms):
	tc=0
	done=[]
	for i in range(len(ms)):
		c=0
		if ms[i] in done:
			continue
		for j in range(len(arr)):
			if ms[i] in arr[j]:
				c+=1
			else:
				continue
		if c==len(arr):
			tc+=1
			done.append(ms[i])
	print(tc)


n = int(input())
arr = []
m=101
ms=''
for _ in range(n):
    arr_item = input()
    arr.append(arr_item)
    if len(arr_item)<m:
    	m=len(arr_item)
    	ms=''.join(arr_item)
gemstones(arr,ms)