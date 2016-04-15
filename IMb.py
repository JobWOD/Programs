def MCDExt(a,b):
	v = [a,b]
	x = [1,0] 
	y = [0,1]
	i = 1
	q = [[]]
	while (v[i] != 0): 
		q = q + [v[i-1] // v[i]]
		v = v + [v[i-1] % v[i]]
		x = x + [x[i-1] - q[i]*x[i]]
		y = y + [y[i-1] - q[i]*y[i]]
		i = i+1
	return (v[i-1])

def inv_mult(a,n):
 if(MCDExt(a,n)!=1):
  print("No tiene inverso multiplicativo.")
 else:
  for i in range(1,n) :
   if( ( a*i-1 )%n == 0 ):
    return i

print(inv_mult (101,1999))

print(inv_mult (1999,101))