
#!/bin/python3

fl=[]
mi=9999999999999
ma=0
def dna_health(mi,ma):
	h=0
	for i in range(first,last+1):
		c=0
		for j in range(len(d)):
			if d[j:j+len(genes[i])]==genes[i]:
				c+=1
		h+=c*health[i]
		if h<ma and h>mi:
			break
	if h<mi:
		mi=h
		fl.append(mi)
	elif h>ma:
		ma=h
		fl.append(ma)


n = int(input())
genes = input().rstrip().split()
health = list(map(int, input().rstrip().split()))
s = int(input())

for s_itr in range(s):
    firstLastd = input().split()
    first = int(firstLastd[0])
    last = int(firstLastd[1])
    d = firstLastd[2]

    dna_health(mi,ma)

print(min(fl),max(fl))

