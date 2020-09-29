"""
Consulte a documentação do strtest para mais detalhes: https://github.com/Insper/python-string-test-runner

Guia rápido:
===========
O TestCaseWrapper possui os seguintes atributos:
    - function: função fornecida pelo usuário
    - program: função que executa o programa fornecido pelo usuário
    - module: arquivo fornecido pelo usuário carregado como um módulo Python
Asserts úteis:
    - assert_similar(self, string1, string2, dist_max=1, case_sensitive=False, msg=None)
    - assert_printed(self, value, index=None, msg=None)
    - assert_printed_all(self, values, msg=None, **kwargs)
Mocks (todas as funções tem os atributos calls, args e kwargs, que guardam a quantidade de chamadas realizadas e os argumentos):
    - mock_print: atributo printed guarda a lista de strings impressas
    - mock_input: atributo input_list recebe uma sequência de entradas a serem utilizadas
    - mock_open: atributo opened é uma lista de arquivos que não foram fechados e é possível adicionar arquivos falsos no dicionário files (chave é o nome do arquivo e o valor é o seu conteúdo)
    - mock_random: chaves são tuplas com os argumentos esperados e valores são sequências de números

Se for implementar os métodos setUpClass, setUp e tearDown lembre-se de chamar a função da classe mãe.
"""
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 3  # Segundos

     
    def test_1(self):
        alunos= [
            {'matricula' : 123, 'PI' : 7, 'PF': 3},
            {'matricula' : 456, 'PI' : 4, 'PF': 8},
            {'matricula' : 789, 'PI' : 5, 'PF': 1},
            {'matricula' : 848, 'PI' : 10, 'PF': 0},
            {'matricula' : 357, 'PI' : 1, 'PF': 2}
        ]
        resultado_obtido = self.function(alunos)
        self.assertIn(789, resultado_obtido, msg=f'A função não devolveu o resultado esperado para a lista {alunos}')
        self.assertIn(357, resultado_obtido, msg=f'A função não devolveu o resultado esperado para a lista {alunos}')
        self.assertEqual(2, len(resultado_obtido), msg=f'Colocou mais alunos de DP do que deveria! Entrada de teste utilizada: {alunos}')
    