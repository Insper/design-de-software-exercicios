from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([])
        self.assertEqual([], resposta)

    def test_2(self):
        resposta = self.function([1, 3, 2, 3, 4, 6, 5])
        self.assertEqual([1, 3, 4, 6], resposta)

    def test_3(self):
        resposta = self.function([10, 1, 2, 3])
        self.assertEqual([10], resposta)

    def test_4(self):
        resposta = self.function([1, 1, 2, 2, 3, 3])
        self.assertEqual([1, 2, 3], resposta)

    def test_5(self):
        resposta = self.function([10, 15, 11, 12, 13, 14])
        self.assertEqual([10, 15], resposta)
