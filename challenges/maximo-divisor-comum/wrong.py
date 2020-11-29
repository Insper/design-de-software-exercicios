def maximo_divisor_comum(x,y):
    r=x%y
    while r>0:
        r=x%y
        if r ==0: 
            return y
        else:
            q=r
            x=q
            y=r
