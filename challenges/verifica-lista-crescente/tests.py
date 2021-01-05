from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([])
        self.assertTrue(resposta)

    def test_2(self):
        resposta = self.function([1])
        self.assertTrue(resposta)

    def test_3(self):
        resposta = self.function([1, 1])
        self.assertFalse(resposta)

    def test_4(self):
        resposta = self.function([1, 2])
        self.assertTrue(resposta)

    def test_5(self):
        resposta = self.function([-4, -2, 1, 2, 3, 4, 5, 10])
        self.assertTrue(resposta)

    def test_5(self):
        resposta = self.function([-4, -2, 1, 2, 3, 4, 5, 2, 10])
        self.assertFalse(resposta)
