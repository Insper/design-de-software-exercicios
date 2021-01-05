from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        resultados = [1, 2, 6, 24, 120, 720, 5040]
        for i, esperado in enumerate(resultados):
            resultado = self.function(i+1)
            self.assertEqual(esperado, resultado)
