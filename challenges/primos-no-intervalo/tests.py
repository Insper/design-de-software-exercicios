from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function(10, 9)
        self.assertEqual([], resposta, 'Não funcionou para o intervalo [10, 9]')

    def test_2(self):
        resposta = self.function(-4, 9)
        self.assertEqual([2, 3, 5, 7], resposta, 'Não funcionou para o intervalo [-4, 9]')

    def test_3(self):
        resposta = self.function(50, 100)
        self.assertEqual([53, 59, 61, 67, 71, 73, 79, 83, 89, 97], resposta, 'Não funcionou para o intervalo [50, 100]')

    def test_4(self):
        resposta = self.function(54, 58)
        self.assertEqual([], resposta, 'Não funcionou para o intervalo [54, 58]')
