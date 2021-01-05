import math

import random

dinheiro = 100
while dinheiro > 0:
    print("Você tem {0} dinheiros".format(dinheiro))
    aposta = int(input("Digite sua aposta: "))
    if aposta > dinheiro:
        print("Você não tem dinheiro o suficiente")
        continue
    if aposta <= 0:
        break
    tipo = input("você vai apostar pelo Número(n) ou por Paridade(p): ")
    if tipo == 'n' or tipo == 'N':
        numero = int(input("Em qual número você vai apostar: "))
        if numero > 36 or numero < 1:
            print("Digite um número entre 1 e 36")
            continue
    else:  #estou suponto que o usuário digitará um valor válido
        paridade = input("Você vai apostar no Par(p) ou Ímpar(i): ")

    sorteio = random.randint(0, 36)
    print("Número sorteado = {0}".format(sorteio))

    if tipo == 'n' or tipo == 'N':
        if numero == sorteio:
            dinheiro += aposta * 35
        else:
            dinheiro -= aposta
    else:
        if ((sorteio % 2 == 0) and (paridade == "p" or paridade == "P")) or (
            (sorteio % 2 == 1) and (paridade == 'i' or paridade == 'I')):
            dinheiro += aposta
        else:
            dinheiro -= aposta
print("Você terminou com {0} dinheiros".format(dinheiro))
