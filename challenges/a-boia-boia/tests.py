from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        all_args = [
            ((16,24,6), True),
            ((10,100,5), True),
            ((12,6,3), False),
            ((1000,100,10), False),
            ((0.01,1,1), True),
        ]
        for args, esperado in all_args:
            obtido = self.function(*args)
            self.assertEqual(obtido, esperado, msg=f'Não funcionou para o peso:{args[0]}, R:{args[1]} e r{args[2]}. Você falou que {("não flutua", "flutua")[obtido]} quando na verdade {("não flutua", "flutua")[esperado]}. Verifique se utilizou as unidades corretas.')
