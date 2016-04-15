def MCDS (a,b):
    n = a
    d = b
    r = n - (d * (n / d))
    while r != 0:
    	n = d
        d = r
        r = n - (d * (n / d))
    return d

print MCDS (1547,560)
c = 0
for i in range (3,1000):
	if MCDS (2,i) == 1:
		c += 1
print "Hay", c, "numeros primos entre 1 y 1000"






