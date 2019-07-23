#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    s=[]
    for c in i:
        if not s:
            s.append(c)
        else:
            if s[-1] == c:
                s.pop()
            else:
                s.append(c)
             
    if not s:
        print ("Empty String")
    else:
        print (''.join(s))

i = input()
result = superReducedString(i)

