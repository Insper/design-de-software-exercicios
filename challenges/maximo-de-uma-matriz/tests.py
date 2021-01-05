from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Falhou para um caso somente com números negativos')
    def test_1(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    @str_test.error_message('Falhou para o caso da matriz nula')
    def test_2(self):
        self.assertAlmostEquals(self.function([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    @str_test.error_message('Falhou para um caso com o maior elemento na primeira linha')
    def test_3(self):
        self.assertAlmostEquals(self.function([[10, 2, 3], [4, 5, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na primeira linha')
    def test_4(self):
        self.assertAlmostEquals(self.function([[1, 10, 3], [4, 5, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na primeira linha')
    def test_5(self):
        self.assertAlmostEquals(self.function([[1, 2, 10], [4, 5, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na segunda linha')
    def test_6(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [10, 5, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na segunda linha')
    def test_7(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 10, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na segunda linha')
    def test_8(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 5, 10], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na terceira linha')
    def test_9(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 5, 6], [10, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na terceira linha')
    def test_10(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 5, 6], [7, 10, 9]]), 10)

    @str_test.error_message('Falhou para um caso com o maior elemento na terceira linha')
    def test_11(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [4, 5, 6], [7, 8, 10]]), 10)

    @str_test.error_message('Falhou para um caso com número negativo')
    def test_12(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [-10, 5, 6], [7, 8, 9]]), 10)

    @str_test.error_message('Falhou para um caso com número negativo')
    def test_13(self):
        self.assertAlmostEquals(self.function([[1, 2, 3], [-10, 5, 6], [20, 8, 9]]), 20)
