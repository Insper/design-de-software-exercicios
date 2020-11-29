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

    def teste_troco1(self):
        notas=[100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
        esperado = ['1 nota(s) de R$ 50', '1 nota(s) de R$ 20', '1 nota(s) de R$ 5', '1 moeda(s) de R$ 1', '1 moeda(s) de R$ 0.5']
        resultado_obtido = self.function(123.50, 200, notas)
        self.assertEqual(resultado_obtido,esperado, msg=f'O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Esperado: {esperado}')

    def teste_troco2(self):
        notas=[100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
        esperado = ['9 nota(s) de R$ 100', '1 nota(s) de R$ 50', '2 nota(s) de R$ 20', '1 nota(s) de R$ 5', '1 nota(s) de R$ 2', '1 moeda(s) de R$ 0.5', '1 moeda(s) de R$ 0.25']
        resultado_obtido = self.function(2.25, 1000, notas)
        self.assertEqual(resultado_obtido,esperado, msg=f'O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Esperado: {esperado}')

    def teste_sem_troco(self):
        notas=[100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
        esperado = []
        resultado_obtido = self.function(10, 10, notas)
        self.assertEqual(resultado_obtido,esperado, msg=f'O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Esperado: {esperado}')