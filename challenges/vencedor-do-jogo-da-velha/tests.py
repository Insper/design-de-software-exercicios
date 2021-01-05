from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        all_args = [
            ([['X', 'O', 'X'], ['.', 'O', 'X'], ['O', '.', 'X']], 'X'),
            ([['X', 'X', 'X'], ['.', 'O', 'O'], ['O', '.', 'X']], 'X'),
            ([['X', 'O', 'O'], ['.', 'O', 'X'], ['X', 'X', 'X']], 'X'),
            ([['X', 'O', 'O'], ['.', 'O', 'X'], ['O', '.', 'X']], 'O'),
            ([['X', '.', 'X'], ['O', 'O', 'O'], ['.', 'O', 'X']], 'O'),
            ([['O', '.', 'X'], ['X', 'O', 'O'], ['.', 'X', 'O']], 'O'),
            ([['X', '.', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']], 'V'),
            ([['O', '.', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']], 'V'),
            ([['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'O', 'X']], 'V'),
        ]
        for args, esperado in all_args:
            obtido = self.function(args)
            self.assertEqual(obtido, esperado, msg=f"Não funcionou para o jogo:{args}. Você falou que o resultado é '{obtido}' mas não é.")
