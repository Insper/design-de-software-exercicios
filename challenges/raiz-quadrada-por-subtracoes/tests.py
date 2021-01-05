from strtest import str_test


def gabarito(valor):
    counter = 0
    while valor > 0:
        valor = valor - (2 * counter + 1)
        counter += 1
    return counter


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_raiz_quadrada(self):
        for numero in range(100):
            resultado_esperado = gabarito(numero**2)
            resultado_obtido = self.function(numero**2)
            self.assertEqual(
                resultado_esperado, resultado_obtido,
                'Não funcionou para o número {0}\n era esperado o valor {1} e foi obtido obt{2}'
                .format(numero, resultado_esperado, resultado_obtido))
