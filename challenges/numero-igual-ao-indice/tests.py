from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([1, 3, 2, 4])
        self.assertEqual(1, len(resposta))
        self.assertTrue(2 in resposta)

    def test_2(self):
        resposta = self.function([0, 10, 2, 30, 4])
        self.assertEqual(3, len(resposta))
        self.assertTrue(0 in resposta)
        self.assertTrue(2 in resposta)
        self.assertTrue(4 in resposta)

    def test_3(self):
        resposta = self.function([5, 4, 3, 2, 1])
        self.assertEqual(0, len(resposta))
