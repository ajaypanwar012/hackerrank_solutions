#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    l=[0 for i in range(max(arr)+1)]
    for i in range(len(l)):
    	for j in range(len(arr)):
    		if i==arr[j]:
    			l[i]+=1
    		else:
    			pass
    print(" ".join(str(i) for i in l))

    
n = int(input())
arr = list(map(int, input().rstrip().split()))

result = countingSort(arr)