from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        all_args = [
            ([[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.9, 10, 10, 10], [10, 10, 9.9, 9.9], [0.0, 9.9, 10, 9.9], [10, 9.8, 10, 10]], 269.3),
            ([[10, 10, 9.9, 10], [9.9, 10, 10, 9.9], [10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10], [9.9, 10, 10, 10], [10, 10, 10, 10], [0, 10, 10, 10], [10, 10, 10, 10]], 269.9),
            ([[9.7, 9.9, 9.7, 9.8], [9.7, 9.9, 9.7, 10], [10, 10, 10, 10], [10, 10, 10, 10], [9.4, 9.6, 9.8, 10], [9.9, 9.9, 9.9, 10], [10, 10, 10, 10], [0, 9.8, 9.8, 9.8], [10, 10, 9.8, 10]], 267.6),
        ]
        for lista, esperado in all_args:
            obtido = self.function(lista)
            self.assertEqual(obtido, esperado, msg=f'Não funcionou para valores: {lista}. Valor esperado: {esperado}. Valor obtido: {obtido}')
