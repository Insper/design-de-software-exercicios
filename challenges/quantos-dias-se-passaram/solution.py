def dias_do_ano(data):
    dia=int(data[0:2])
    mes=int(data[3:5])
    if (dia==1 and mes==1):
        return 0
    meses=[31,28,31,30,31,30,31,31,30,31,30,31]
    soma=0
    for i in range(0,mes-1):
        soma+=meses[i]
    return soma+dia-1