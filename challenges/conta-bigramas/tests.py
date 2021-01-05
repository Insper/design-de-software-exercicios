from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['banana nanica']
        esperados = [{'ba': 1, 'an': 3, 'na': 3, 'a ': 1, ' n': 1, 'ni': 1, 'ic': 1, 'ca': 1}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a string {0}'.format(entrada))
