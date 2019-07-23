#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
	l=[]
	m=9999999
	md=[]
	arr = arr+arr
	arr.sort()
	arr.pop(0)
	arr.pop()

	for i in range(len(arr)-1):
		sl=[arr[i],arr[i+1]]
		l.append(sl)

	for i in range(len(l)):
		if (l[i][1]-l[i][0])<m and (l[i][1]-l[i][0])>0:
			md=[]
			m=(l[i][1]-l[i][0])
			md.append(l[i][0])
			md.append(l[i][1])
		elif (l[i][1]-l[i][0])==m and (l[i][1]-l[i][0])>0:
			md.append(l[i][0])
			md.append(l[i][1])
	for i in md:
		print(i,end=' ')






n = int(input())

arr = list(map(int, input().rstrip().split()))

result = closestNumbers(arr)
