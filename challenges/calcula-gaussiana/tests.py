from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Verificar quando sigma é 1 e as outras entradas são 0')
    def test_1(self):
        self.assertAlmostEquals(self.function(0, 0, 1), 0.3989422804014327)

    @str_test.error_message('Verificar quando sigma é 1 e as outras entradas são positivas')
    def test_2(self):
        self.assertAlmostEquals(self.function(100, 100, 1), 0.3989422804014327)

    @str_test.error_message('Verificar quando sigma é 0,1 e as outras entradas são números opostos com valor absoluto alto (ex. 1.000.000 e -1.000.000)')
    def test_3(self):
        self.assertAlmostEquals(self.function(-100000, 100000, 0.1), 0)

    @str_test.error_message('Verificar quando sigma é 0,1 e as outras entradas são números opostos com valor absoluto alto (ex. 1.000.000 e -1.000.000)')
    def test_4(self):
        self.assertAlmostEquals(self.function(100000, -100000, 0.1), 0)

    @str_test.error_message('Verificar quando sigma é o inverso da raíz de 2 pi')
    def test_5(self):
        self.assertAlmostEquals(self.function(0, 0, 0.3989422804014327), 1)

    @str_test.error_message('Verificar quando x ou mi é igual a 0 e os outros valores são o inverso da raíz de 2 pi')
    def test_6(self):
        self.assertAlmostEquals(self.function(0.3989422804014327, 0, 0.3989422804014327), 0.6065306597126334)

    @str_test.error_message('Verificar quando x ou mi é igual a 0 e os outros valores são o inverso da raíz de 2 pi')
    def test_7(self):
        self.assertAlmostEquals(self.function(0, 0.3989422804014327, 0.3989422804014327), 0.6065306597126334)
