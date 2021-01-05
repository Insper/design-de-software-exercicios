from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def compare_lists(self, result, expected, msg=''):
        self.assertEqual(
            len(result),
            len(expected),
            msg=msg +
            'Resultado tem uma quantidade de elementos diferente do esperado. Obtido: {0}. Esperado: {1}.'
            .format(result, expected))
        self.assertEqual(
            sorted(result),
            sorted(expected),
            msg=msg +
            'Não possui todos os elementos esperados. Obtido: {0}. Esperado: {1}.'
            .format(result, expected))

    def test_1(self):
        self.compare_lists(self.function(''), [],
                           msg='Falhou para string vazia. ')

    def test_2(self):
        self.compare_lists(self.function('a'), ['a'],
                           msg='Falhou para string com uma letra. ')

    def test_4(self):
        self.compare_lists(self.function('abcd'),
                           ['abcd', 'bcd', 'cd', 'd'],
                           msg='Falhou para a string "abcd". ')

    def test_5(self):
        self.compare_lists(self.function('abcdefgh'), [
            'abcdefgh', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h'
        ],
                           msg='Falhou para a string "abcdefgh". ')
