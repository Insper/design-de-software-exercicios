from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([], [])
        self.assertEqual(0, resposta, 'Não funcionou para nota vazia')

    def test_2(self):
        resposta = self.function([10], [2])
        self.assertEqual(20, resposta, 'Não funcionou para nota com um item')

    def test_3(self):
        resposta = self.function([10, 5, 2], [2, 3, 9])
        self.assertEqual(53, resposta, 'Não funcionou para a entrada [10, 5, 2], [2, 3, 9]')
