from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Falhou para algum teste com idade de criança')
    def test_1(self):
        self.assertAlmostEquals(self.function(0), 'crianca')

    @str_test.error_message('Falhou para algum teste com idade de criança')
    def test_2(self):
        self.assertAlmostEquals(self.function(11), 'crianca')

    @str_test.error_message('Falhou para algum teste com idade de adolescente')
    def test_3(self):
        self.assertAlmostEquals(self.function(12), 'adolescente')

    @str_test.error_message('Falhou para algum teste com idade de adolescente')
    def test_4(self):
        self.assertAlmostEquals(self.function(17), 'adolescente')

    @str_test.error_message('Falhou para algum teste com idade de adulto')
    def test_5(self):
        self.assertAlmostEquals(self.function(18), 'adulto')

    @str_test.error_message('Falhou para algum teste com idade de adulto')
    def test_6(self):
        self.assertAlmostEquals(self.function(100), 'adulto')
