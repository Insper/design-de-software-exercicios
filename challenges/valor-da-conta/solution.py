def Valor_10_percent(conta_restaurante):
    x=0.1*conta_restaurante + conta_restaurante
    return x

conta_restaurante= float(input("Diga a conta do restaurante: "))
total = Valor_10_percent(conta_restaurante)
print ("Valor da conta com 10%: R$ {0:.2f}".format(total))
