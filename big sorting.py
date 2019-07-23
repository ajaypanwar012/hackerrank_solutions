#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    print('\n'.join(sorted(unsorted,key=int)))

n = int(input())
unsorted = []

for _ in range(n):
    unsorted_item = (input())
    unsorted.append(unsorted_item)

bigSorting(unsorted)
