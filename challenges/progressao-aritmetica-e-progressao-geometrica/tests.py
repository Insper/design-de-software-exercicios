from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Falhou para caso NA')
    def test_1(self):
        self.assertEqual(self.function([0, 1, -1]), 'NA')

    @str_test.error_message('Falhou para caso AG')
    def test_2(self):
        self.assertEqual(self.function([100, 100, 100, 100, 100]), 'AG')

    @str_test.error_message('Falhou para PA de razão positiva')
    def test_3(self):
        self.assertEqual(self.function([132, 169, 206, 243, 280]), 'PA')

    @str_test.error_message('Falhou para PG de razão positiva')
    def test_4(self):
        self.assertEqual(self.function([11, 33, 99, 297, 891, 2673, 8019, 24057, 72171, 216513]), 'PG')

    @str_test.error_message('Falhou quando um dos termos não completa a PA')
    def test_5(self):
        self.assertEqual(self.function([0, 132, 169, 206]), 'NA')

    @str_test.error_message('Falhou quando um dos termos não completa a PA')
    def test_6(self):
        self.assertEqual(self.function([132, 169, 206, 10]), 'NA')

    @str_test.error_message('Falhou quando um dos termos não completa a PG')
    def test_7(self):
        self.assertEqual(self.function([1, 11, 33, 99, 297, 891, 2673]), 'NA')

    @str_test.error_message('Falhou quando um dos termos não completa a PG')
    def test_8(self):
        self.assertEqual(self.function([11, 33, 99, 297, 891, 2673, 1]), 'NA')

    @str_test.error_message('Falhou para PG de razão entre 0 e 1')
    def test_9(self):
        self.assertEqual(self.function([-4.0, -2.0, -1.0, -0.5, -0.25, -0.125, -0.0625]), 'PG')

    @str_test.error_message('Falhou para PA com razão negativa')
    def test_10(self):
        self.assertEqual(self.function([-14, -18, -22, -26, -30]), 'PA')

    @str_test.error_message('Falhou para PG de razão negativa')
    def test_11(self):
        self.assertEqual(self.function([-2, 4, -8, 16, -32, 64, -128, 256, -512, 1024]), 'PG')
