from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for n in list(range(1, 101)) + [200, 500, 1000, 4247]:
            esperado = round(n**.5)
            obtido = self.function(n)
            msg = 'Não funcionou para n={0}. Esperado={1}. Obtido={2}'.format(
                n, esperado, obtido)
            self.assertEqual(esperado, obtido, msg=msg)
