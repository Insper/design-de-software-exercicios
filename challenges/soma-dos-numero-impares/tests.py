from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([])
        self.assertEqual(0, resposta, 'Não funcionou para lista vazia')

    def test_2(self):
        resposta = self.function([1, 2, 3])
        self.assertEqual(4, resposta, 'Não funcionou para a lista [1, 2, 3]')

    def test_3(self):
        resposta = self.function([2, 5])
        self.assertEqual(5, resposta, 'Não funcionou para a lista [2, 5]')

    def test_4(self):
        resposta = self.function([54, 58, 24])
        self.assertEqual(0, resposta, 'Não funcionou para a lista [54, 58, 24]')
