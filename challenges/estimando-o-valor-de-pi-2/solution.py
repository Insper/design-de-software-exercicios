def PiWallis(n):
    pi = 1
    i = 0
    num = 2
    den = 1
    while i < n:
        pi *= num/den
        if i % 2 == 0:
            den += 2
        else:
            num += 2
        i += 1
    return pi * 2