from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        args = [
            ([275, 290, 310, 390, 480], [75, 180, 120, 110, 150], 348.42),
            ([1, 4], [2, 6], 5),
            ([1, 1, 2, 2, 3], [3, 4, 4, 5, 5], 4)
        ]
        for x, y, esperado in args:
            obtido = self.function(x, y)
            self.assertAlmostEqual(obtido, esperado, places=1, msg=f'Não funcionou para as listas {x} e {y}. Valor esperado: {esperado}. Valor obtido: {obtido}')
