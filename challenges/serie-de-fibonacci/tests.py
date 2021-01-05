from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function(1)
        self.assertEqual([1], resposta, 'Não funcionou para a entrada 1')

    def test_2(self):
        resposta = self.function(2)
        self.assertEqual([1, 1], resposta, 'Não funcionou para a entrada 2')

    def test_3(self):
        resposta = self.function(3)
        self.assertEqual([1, 1, 2], resposta, 'Não funcionou para a entrada 3')

    def test_4(self):
        resposta = self.function(4)
        self.assertEqual([1, 1, 2, 3], resposta, 'Não funcionou para a entrada 4')

    def test_5(self):
        resposta = self.function(5)
        self.assertEqual([1, 1, 2, 3, 5], resposta, 'Não funcionou para a entrada 5')

    def test_6(self):
        resposta = self.function(6)
        self.assertEqual([1, 1, 2, 3, 5, 8], resposta, 'Não funcionou para a entrada 6')

    def test_7(self):
        resposta = self.function(7)
        self.assertEqual([1, 1, 2, 3, 5, 8, 13], resposta, 'Não funcionou para a entrada 7')

    def test_8(self):
        resposta = self.function(8)
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21], resposta, 'Não funcionou para a entrada 8')

    def test_9(self):
        resposta = self.function(9)
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34], resposta, 'Não funcionou para a entrada 9')

    def test_10(self):
        resposta = self.function(10)
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], resposta, 'Não funcionou para a entrada 10')
