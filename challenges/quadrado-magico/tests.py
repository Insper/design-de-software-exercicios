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

    def test_matriz_3x3(self):
        resultado_obtido = self.function([[2, 7, 6],[9, 5, 1],[4, 3, 8]])
        self.assertTrue(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Deveria ter identificado o quadrado mágico na matriz [[2, 7, 6],[9, 5, 1],[4, 3, 8]]')

    def test_matriz_5x5(self):
        resultado_obtido = self.function([[23, 6, 19, 2, 15],[4, 12, 25, 8, 16],[10, 18, 1, 14, 22],[11, 24, 7, 20, 3],[17, 5, 13, 21, 9]])
        self.assertTrue(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Deveria ter identificado o quadrado mágico na matriz [[23, 6, 19, 2, 15],[4, 12, 25, 8, 16],[10, 18, 1, 14, 22],[11, 24, 7, 20, 3],[17, 5, 13, 21, 9]]')

    def test_matriz_false_3x3(self):
        resultado_obtido = self.function([[4, 5, 7],[3, 6, 8],[7, 8, 9]])
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Não deveria ter identificado o quadrado mágico na matriz [[4, 5, 7],[3, 6, 8],[7, 8, 9]]')

    def test_matriz_false_4x4(self):
        resultado_obtido = self.function([[16, 23, 17], [78, 32, 21], [17, 16, 15]])
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Não deveria ter identificado o quadrado mágico na matriz [[16, 23, 17], [78, 32, 21], [17, 16, 15]]')