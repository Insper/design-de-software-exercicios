from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['babador', 'aaaa']
        esperados = [['ba', 'ab', 'ad', 'do', 'or'], ['aa']]
        for entrada, esperado in zip(entradas, esperados):
            recebido = self.function(entrada)
            self.assertEqual(len(esperado), len(recebido), 'Não funcionou para a entrada {0}'.format(entrada))
            for bigrama in esperado:
                self.assertTrue(bigrama in recebido, 'Resposta não contém o bigrama {0} para a string {1}'.format(bigrama, entrada))
