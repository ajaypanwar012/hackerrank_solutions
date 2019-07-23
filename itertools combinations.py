# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
fl=[]
l=[]
str,n=input().split()
for i in range(1,int(n)+1):
    l=list(combinations(str,i)
    for j in l:
        fl.append(j)
for i in fl:
    for j in i:
        print(j,end="")
    print()
