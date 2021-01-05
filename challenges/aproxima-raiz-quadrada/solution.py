def aproxima_raiz(n):
    raiz_exata = n**(1/2)
    raiz_baixo = raiz_exata//1
    raiz_cima = raiz_baixo+1
    if (n-raiz_baixo**2)<(raiz_cima**2-n):
        return raiz_baixo
    else:
        return raiz_cima