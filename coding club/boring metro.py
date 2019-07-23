l=[]
t=int(input())
for i in range(t):
	n = int(input())
	nl = list(map(int,input().split()))
	c=1
	flag=0
	for i in range(len(nl)-1):
		m=nl[i]
		if flag==0:
			if nl[i+1]<m:
				c+=1
				flag=1
		if flag==1:
			if nl[i+1]>=m:
				flag=0
	if flag==0:
		c+=1
	l.append(c)
for j in l:
	print(j)
