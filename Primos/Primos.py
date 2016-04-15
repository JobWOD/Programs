def Primos (a):
	if a < 2:
		return False
	for i in range (2,a):
		if a % i == 0:
			return False
	return True

def PrimosR (x,y):
	c = 0
	for i in range (x,y):
		if Primos(i) == True:
			c = c + 1
			print i
	return c

c = PrimosR(0,1000)
print PrimosR(0,1000)
print "hay", c , "numeros primos entre 0 y 1000"
