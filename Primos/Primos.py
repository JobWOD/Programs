def Primos (a):
	if a < 2:
		return False
	for i in range (2,a):
		if a % i == 0:
			return False
		else:
			return True


def PrimosR (a,b):
	c = 0
	for i in range (a,b):
		if Primos(i) == True:
			c += 1
	return c


print PrimosR (0,1000)
