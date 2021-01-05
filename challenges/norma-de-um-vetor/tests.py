from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Falhou para lista de tamanho 1')
    def test_1(self):
        self.assertAlmostEquals(self.function([1]), 1)

    @str_test.error_message('Falhou para lista de tamanho 2')
    def test_2(self):
        self.assertAlmostEquals(self.function([3, 4]), 5)

    @str_test.error_message('Falhou para lista de tamanho 3')
    def test_3(self):
        self.assertAlmostEquals(self.function([1, 2, 3]), 3.7416573867739413)

    @str_test.error_message('Falhou para lista de tamanho maior que 3')
    def test_4(self):
        self.assertAlmostEquals(self.function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 19.621416870348583)

    @str_test.error_message('Falhou para lista de tamanho maior que 3')
    def test_5(self):
        self.assertAlmostEquals(self.function([1, 1, 1, 1, 1, 1, 1, 1, 1]), 3)
