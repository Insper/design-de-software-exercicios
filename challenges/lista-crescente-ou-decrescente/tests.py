from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        C = 'crescente'
        D = 'decrescente'
        N = 'nenhum'

        testes = [
            ([], N),
            ([100], N),
            ([1, 4], C),
            ([7, 2], D),
            (list(range(2, 10, 2)), C),
            (list(range(10, 0, -2)), D),
            ([1, 5, 2, 7, 3, 7, 4], N),
            (list(range(100)) + list(range(100, 0, -1)), N),
            (list(range(100, 0, -1)) + list(range(100)), N),
        ]
        for arg, esperado in testes:
            obtido = self.function(arg)
            msg = 'Não funcionou para a lista {0}. Esperado: {1}. Obtido: {2}'.format(
                arg, repr(esperado), repr(obtido))
            self.assertEqual(esperado, obtido, msg=msg)
