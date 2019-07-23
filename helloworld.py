# Complete the strangeCounter function below.
def strangeCounter(t):
	a=3
	v=3
	while(t>a):
		a = a + v*2
		v*=2
	x=v-2
	f = v-(t-x)
	return f

t = int(input())
print(strangeCounter(t))
