from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resposta = self.function(['fabio'], ['ayres'])
        self.assertEqual(['fabio ayres'], resposta)

    def test_2(self):
        resposta = self.function(['fabio', 'raul', 'andrew'], ['ayres', 'ikeda', 'kurauchi'])
        self.assertEqual(['fabio ayres', 'raul ikeda', 'andrew kurauchi'], resposta)
