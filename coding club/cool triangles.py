import math
l=[]
t=int(input())
for i in range(t):
	ab=(input().split())
	a=int(ab[0])
	b=int(ab[1])
	if math.sqrt((a*a)+(b*b))==int(math.sqrt((a*a)+(b*b))):
		l.append("yes")
	elif (((a*a)-(b*b))>0) and (math.sqrt((a*a)-(b*b))==int(math.sqrt((a*a)-(b*b)))):
		l.append("yes")
	elif ((b*b)-(a*a))>0 and (math.sqrt((b*b)-(a*a))==int(math.sqrt((b*b)-(a*a)))):
		l.append("yes")
	else:
		l.append("no")
for i in l:
	print(i)