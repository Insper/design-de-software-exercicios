def calcula_extensao(xs, ys):
    extensao = 0
    i = 0
    while i < len(xs) - 1:
        extensao += ((xs[i+1]-xs[i])**2 + (ys[i+1]-ys[i])**2)**.5
        i += 1
    return extensao
