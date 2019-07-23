#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
	arr.sort()
	print(arr)
	m = (len(arr)//2)
	print(arr[m])

n = int(input())

arr = list(map(int, input().rstrip().split()))

findMedian(arr)