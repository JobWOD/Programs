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






