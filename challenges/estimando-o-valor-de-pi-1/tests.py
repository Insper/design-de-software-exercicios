from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for n in [1, 2, 3, 4, 10, 100, 1000, 10000]:
            s = 0
            for i in range(1, n + 1):
                s += 6 / (i**2)
            esperado = s**0.5
            obtido = self.function(n)
            msg = 'Não funcionou para n={0}. Esperado={1}. Obtido={2}'.format(
                n, esperado, obtido)
            if abs(obtido - s) < 0.01:
                msg += ' Será que você não se esqueceu da raíz quadrada?'
            self.assertAlmostEqual(esperado, obtido, msg=msg)
