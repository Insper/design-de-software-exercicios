def maximo_divisor_comum(x,y):
    if x == y:
        return x
    r=x%y
    while r>0:
        r=x%y
        if r ==0: 
            return y
        else:
            q=y
            x=q
            y=r
