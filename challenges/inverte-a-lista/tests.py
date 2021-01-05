from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function([])
        self.assertEqual([], resposta)

    def test_2(self):
        resposta = self.function([1])
        self.assertEqual([1], resposta)

    def test_3(self):
        resposta = self.function([1, 2, 3, 4])
        self.assertEqual([4, 3, 2, 1], resposta)

    def test_4(self):
        resposta = self.function(['a', 'b', 'c'])
        self.assertEqual(['c', 'b', 'a'], resposta)
