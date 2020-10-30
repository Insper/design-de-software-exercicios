def calcula_troco(preco, dinheiro, notas):
    devolve=[]
    troco = dinheiro - preco
    if troco > 0:
        for p in notas:
            if troco >= p:
                n = troco//p
                r = troco - p*n
                
                if p>1: 
                    devolve.append('%s nota(s) de R$ %s' % (int(n), p))
                else: 
                    devolve.append('%s moeda(s) de R$ %s' % (int(n), p))
                troco = r
    
    return devolve