n = int(input())
s = input()
m = int(input())
ns=''
for i in range(len(s)):
	if s[i].isalnum():
		ns[i]=chr(ord(s[i])+m)
print(ns)