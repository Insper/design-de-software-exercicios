from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        P = 'par'
        I = 'ímpar'
        M = 'misturado'

        testes = [
            ([], M),
            ([100], P),
            ([2, 4], P),
            ([7, 5], I),
            (list(range(2, 10, 2)), P),
            (list(range(1, 13, 2)), I),
            ([1, 5, 2, 7, 3, 7, 4], M),
            (list(range(2, 100, 6)), P),
            (list(range(2, 10, 2)) + [99], M),
            (list(range(7, 101, 8)), I),
            (list(range(7, 21, 2)) + [100], M),
        ]
        for arg, esperado in testes:
            obtido = self.function(arg)
            if obtido is None:
                self.assertFalse(
                    True, msg='Você não se esqueceu do return em algum caso?')
            msg = 'Não funcionou para a lista {0}. Esperado: {1}. Obtido: {2}.'.format(
                arg, repr(esperado), repr(obtido))
            if obtido.lower() == esperado:
                msg += ' Você está escrevendo a resposta com todas as letras em minúscula?'
            if esperado == "ímpar" and obtido.lower() == "impar":
                msg += ' Você está escrevendo ímpar com acento?'
            self.assertEqual(esperado, obtido, msg=msg)
