#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x=arr[-1]
    for i in range(n-1,-1,-1):
        if arr[i-1]>x and i>0:
            arr[i]=arr[i-1]
        else:
            arr[i]=x
            for j in arr:
            	print(j,end=" ")
            print()
            return
        for j in arr:
            print(j,end=" ")
        print()
    
n = int(input())
arr = list(map(int, input().rstrip().split()))

insertionSort1(n, arr)
