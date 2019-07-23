#!/bin/python3
f=[]
def funnyString(s):
	n=s[-1::-1]
	sl=[]
	nl=[]
	for i in range(len(s)-1):
		a=abs(ord(s[i])-ord(s[i+1]))
		sl.append(a)
		b=abs(ord(n[i])-ord(n[i+1]))
		nl.append(b)
		if a!=b:
			f.append("Not Funny")
			break
	if sl==nl:
		f.append("Funny")

q = int(input())

for q_itr in range(q):
    s = input()
    funnyString(s)
for x in f:
	print(x)
