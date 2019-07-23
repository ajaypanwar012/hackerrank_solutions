#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    ngrid=[]
    while(n-1>0):
        ngrid=grid

        for i in range(r):
            for j in range(c):
                if grid[i][j]=='.':
                    grid[i][j]="O"

        n-=1
        if (n>0):
            for i in range(r):
                for j in range(c):
                    if ngrid[i][j]==grid[i][j]:

        # inner elements......

                        if ((i-1>-1) and (j-1>-1)) and ((i+1<=r-1) and (j+1<=c-1)):
                            grid[i][j] = "."
                            grid[i-1][j] = "."
                            grid[i][j-1] = "."
                            grid[i+1][j] = "."
                            grid[i][j+1] = "."

        # corner elements......

                        elif ((i==0) and (j==0)):
                            grid[i][j] = "."
                            grid[i+1][j] = "."
                            grid[i][j+1] = "."
                        elif ((i==0) and (j==c-1)):
                            grid[i][j] = "."
                            grid[i+1][j] = "."
                            grid[i][j-1] = "."
                        elif ((i==r-1) and (j==0)):
                            grid[i][j] = "."
                            grid[i-1][j] = "."
                            grid[i][j+1] = "."
                        elif ((i==r-1) and (j==c-1)):
                            grid[i][j] = "."
                            grid[i][j-1] = "."
                            grid[i-1][j] = "."

        # edge elements.....

                        elif ((i==0) and (j>0)) and (j+1<=c-1):
                            grid[i][j] = "."
                            grid[i][j-1] = "."
                            grid[i+1][j] = "."
                            grid[i][j+1] = "."
                        elif ((i>0) and (j==0)) and (i+1<=r-1):
                            grid[i][j] = "."
                            grid[i-1][j] = "."
                            grid[i+1][j] = "."
                            grid[i][j+1] = "."
                            
                        
                        elif ((i==r-1) and (j<c-1)) and (j>0):
                            grid[i][j] = "."
                            grid[i-1][j] = "."
                            grid[i][j-1] = "."
                            grid[i][j+1] = "."
                        elif ((i<r-1) and (j==c-1)) and (i>0):
                            grid[i][j] = "."
                            grid[i+1][j] = "."
                            grid[i][j-1] = "."
                            grid[i-1][j] = "."
        n-=1
    print(grid)
                
                    

rcn = input().split()
r = int(rcn[0])

c = int(rcn[1])

n = int(rcn[2])

grid = []

for _ in range(r):
    grid_item = input()
    grid.append(grid_item)

result = bomberMan(n, grid)