#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
nl=[]
def absolutePermutation(n, k):
    l=[]
    i=1
    while(i<=n-k):
        l.append(i+k)
        i+=1
    for j in range(k):
        l.append(j+1)
    for i in range(n):
        if abs(l[i]-(i+1))!= k:
            nl.append([-1])
            return -1
    nl.append(l)

t = int(input())

for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    absolutePermutation(n, k)
for i in range(t):
    print(' '.join(map(str,nl[i])))