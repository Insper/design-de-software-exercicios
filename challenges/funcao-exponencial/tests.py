'''
Se pode usar uma série para calcular o valor do e (número de Euler ou Neperiano). Basicamente a ideia é somar uma sequência de número, e conforme se avança na sequência, se chega mais perto do valor desejado. A série de Taylor para calcular e^x é:

e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + x^5/5! + ...

Faça uma função em Python que calcula o resultado do e^x em para uma série de tamanho n. Você pode supor que as entradas para x e n serão sempre números positivos.

Nome da função: calcula_euler(x, n)
'''

from strtest import str_test
import math


def gabarito(x, n, adicionais=3):
    parciais = [0]
    n += adicionais
    for i in range(n):
        parciais.append(parciais[-1] + (x**i) / math.factorial(i))
    parciais = parciais[1:]
    return parciais[-adicionais - 1], parciais


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for x in range(2, 10):
            for n in range(2, 10):
                args = (x, n)
                obtido = self.function(*args)
                esperado, parciais = gabarito(*args)
                msgs = [
                    'Resposta diferente da esperada para x={0}, n={1}. Obtido: {2}. Esperado: {3}'
                    .format(*(args + (obtido, esperado)))
                ]
                if esperado == self.function(n, x):
                    msgs.append(
                        'Argumentos invertidos. A chamada da função assume que o primeiro argumento é o x e o segundo é o n.'
                    )
                for p in parciais:
                    if p == obtido:
                        msgs.append(
                            'Quantidade incorreta de termos na soma. Note que o 1 e o x também contam como termos da soma.'
                        )
                        break
                self.assertAlmostEquals(esperado,
                                        obtido,
                                        msg=' Ou '.join(msgs))
