'''
Um ângulo crítico de refração é definido quando um feixe de luz que atravessa de um meio de índice de refração maior para um menor é refratado paralelo a superfície. Ângulos de incidência maiores que este, farão a luz refletir internamente de forma total, e não mais refratar.

Faça uma função em Python que recebe os valores de n1, n2 e theta1 e informa se foi uma refração ou reflexão interna, para isso crie uma função que recebe os valores e retorne verdadeiro caso seja uma reflexão interna total, ou falso caso seja uma refração. Dica: Um valor de seno maior que 1(um) indica uma reflexão total interna.

Nome da função: reflexao_total_interna(n1, n2, theta1)
'''

from strtest import str_test
from itertools import permutations
import math


def gabarito(n1, n2, teta2):
    sin_t1 = n2 * math.sin(math.radians(teta2)) / n1
    if sin_t1 > 1.0:
        return True
    else:
        return False


def errado(n1, n2, teta1):
    sin_t2 = n2 * math.sin(teta1) / n1
    if sin_t2 > 1.0:
        return True
    else:
        return False


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        iguais = []
        primeiro_erro = None
        msgs = []
        for t2 in range(-90, 90):
            args = (1, 2, t2)
            obtido = self.function(*args)
            esperado = gabarito(*args)
            iguais.append(obtido == esperado)
            if errado(*args) == obtido:
                msgs.append(
                    'Resposta diferente da esperada. Os ângulos são fornecidos em graus, mas as funções trigonométricas do Python utilizam ângulos em radianos.'
                )
            for args_errados in permutations(args):
                try:
                    if args_errados != args and gabarito(
                            *args_errados) == obtido:
                        msgs.append(
                            'Argumentos recebidos na ordem errada. A função foi chamada assumindo a ordem: n1, n2, teta2.'
                        )
                except:
                    pass
            if not msgs:
                msgs.append(
                    'Resposta diferente da esperada para os argumentos n1={0}, n2={1}, teta2={2}. Obtido: {3}. Esperado: {4}'
                    .format(*(args + (obtido, esperado))))
            try:
                self.assertEqual(esperado, obtido, ' Ou '.join(set(msgs)))
            except AssertionError as e:
                primeiro_erro = e
        if all(not i for i in iguais):
            self.assertTrue(
                False,
                'Resposta invertida para todos os testes. Devolveu True quando era esperado False e vice-versa.'
            )
        if primeiro_erro:
            raise primeiro_erro
