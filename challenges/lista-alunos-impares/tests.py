from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [['Aluno 0'], ['Aluno 0', 'Aluno 1', 'Aluno 2'], ['Aluno 0', 'Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4', 'Aluno 5']]
        esperados = [[], ['Aluno 1'], ['Aluno 1', 'Aluno 3', 'Aluno 5']]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
