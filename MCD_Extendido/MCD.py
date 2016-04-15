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
    return (v[i-1], x[i-1], y[i-1])

mcd = MCDExt(1547,560)
print mcd

