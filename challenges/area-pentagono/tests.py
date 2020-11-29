from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 3

    def test_1(self):
        resultado_obtido = self.function(4)
        self.assertAlmostEqual(27.5, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 27.5. Obtido: {resultado_obtido}', places=1)

    def test_2(self):
        resultado_obtido = self.function(0)
        self.assertEqual(0, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 0. Obtido: {resultado_obtido}')

    def test_3(self):
        resultado_obtido = self.function(8)
        self.assertAlmostEqual(110.1, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 110. Obtido: {resultado_obtido}',places=0)
