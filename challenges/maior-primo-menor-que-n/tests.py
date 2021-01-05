from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Falhou para um caso que a resposta deveria ser -1')
    def test_1(self):
        self.assertAlmostEquals(self.function(-10), -1)

    @str_test.error_message('Falhou para um caso que a resposta deveria ser -1')
    def test_2(self):
        self.assertAlmostEquals(self.function(0), -1)

    @str_test.error_message('Falhou para um caso que a resposta deveria ser -1')
    def test_3(self):
        self.assertAlmostEquals(self.function(1), -1)

    @str_test.error_message('Existe um número par que também é primo')
    def test_4(self):
        self.assertAlmostEquals(self.function(2), 2)

    @str_test.error_message('O valor n pode ser um número primo')
    def test_5(self):
        self.assertAlmostEquals(self.function(3), 3)

    @str_test.error_message('Falhou para n > 10')
    def test_6(self):
        self.assertAlmostEquals(self.function(10), 7)

    @str_test.error_message('Falhou para n > 10')
    def test_7(self):
        self.assertAlmostEquals(self.function(1000), 997)
