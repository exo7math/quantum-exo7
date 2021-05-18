

p = 0.1

for n in [10,100,1000]:
	e = (1-p)**n
	p3 = p**2 * (3-2*p)
	ee = (1-p3)**n
	print (p,n,e,ee)
