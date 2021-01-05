from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for n in [1, 2, 3, 4, 10, 100, 1000, 2000, 10000, 100000]:

            numerador = 2.0
            denominador = 1.0
            pi = 1.0
            anterior = pi
            proximo = pi
            for i in range(n):
                anterior = pi
                pi *= numerador / denominador
                if i % 2 == 0:
                    denominador += 2.0
                else:
                    numerador += 2.0
            proximo = pi * numerador / denominador

            pi *= 2.0
            anterior *= 2.0
            proximo *= 2.0

            esperado = pi
            obtido = self.function(n)

            msg = 'Não funcionou para n={0}. Esperado={1}. Obtido={2}.'.format(
                n, esperado, obtido)
            try:
                self.assertAlmostEqual(anterior, obtido)
                msg += ' Será que você não está calculando com um elemento a menos da série?'
            except:
                pass
            try:
                self.assertAlmostEqual(proximo, obtido)
                msg += ' Será que você não está calculando com um elemento a mais da série?'
            except:
                pass
            try:
                self.assertAlmostEqual(anterior / 2, obtido)
                msg += ' Note que o resultado da soma é pi/2, mas queremos o valor de pi.'
            except:
                pass
            try:
                self.assertAlmostEqual(proximo / 2, obtido)
                msg += ' Note que o resultado da soma é pi/2, mas queremos o valor de pi.'
            except:
                pass
            try:
                self.assertAlmostEqual(esperado / 2, obtido)
                msg += ' Note que o resultado da soma é pi/2, mas queremos o valor de pi.'
            except:
                pass
            self.assertAlmostEqual(esperado, obtido, msg=msg)
