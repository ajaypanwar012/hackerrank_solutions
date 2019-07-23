#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
	fac =1
	if n<=1:
		return fac
	else:
		fac =n*factorial(n-1)
		return fac

n = int(input())

print(factorial(n))
















