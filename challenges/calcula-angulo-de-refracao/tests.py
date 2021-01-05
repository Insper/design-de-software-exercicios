'''
A lei de Snell-Descartes define que a relação entre o ângulo de incidência e o ângulo de refração de um raio de luz atravessando de um meio para o outro é inversamente proporcional a razão dos índices de refração dos meios, que é dado pela seguinte fórmula:
n1/n2 = sen(theta2)/sen(theta1)
Faça um programa em Python que pede os valores de n1, n2 e theta1 e retorna o valor do theta2. Os valores passados de n1, n2 são adimensionais, já os valores de theta1 e theta2 deverão ser passados e retornados em graus.

Nome da função: snell_descartes(n1, n2, teta1)
'''

from strtest import str_test
from itertools import permutations
import math


def gabarito(n1, n2, teta1):
    sin_t2 = n1 * math.sin(math.radians(teta1)) / n2
    teta2_r = math.asin(sin_t2)
    return math.degrees(teta2_r)


def errado(n1, n2, teta1):
    sin_t2 = n1 * math.sin(teta1) / n2
    teta2_r = math.asin(sin_t2)
    return teta2_r


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for t1 in range(30, 60):
            args = (1, 2, t1)
            obtido = self.function(*args)
            esperado = gabarito(*args)
            msg = 'Resposta diferente da esperada para os argumentos n1={0}, n2={1}, teta1={2}. Obtido: {3}. Esperado: {4}'.format(
                *(args + (obtido, esperado)))
            if errado(*args) == obtido:
                msg = 'Resposta diferente da esperada. Os ângulos são fornecidos em graus, mas as funções trigonométricas do Python utilizam ângulos em radianos.'
            for args_errados in permutations(args):
                try:
                    if args_errados != args and gabarito(
                            *args_errados) == obtido:
                        msg = 'Argumentos recebidos na ordem errada. A função foi chamada assumindo a ordem: n1, n2, teta1.'
                except:
                    pass
            self.assertAlmostEqual(esperado, obtido, msg=msg)
