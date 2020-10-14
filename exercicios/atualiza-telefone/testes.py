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

    def test_atualizado(self):
        resultado_obtido = self.function("999999999")
        self.assertEqual(resultado_obtido,("999999999"), msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Telefone: '999999999'.")

    def test_atualizado_traco(self):
        resultado_obtido = self.function("99999-9999")
        self.assertEqual(resultado_obtido,("99999-9999"), msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Telefone: '99999-9999'.")

    def test_desatualizado_traco(self):
        resultado_obtido = self.function("8888-8888")
        self.assertEqual(resultado_obtido,("98888-8888"), msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Telefone: '8888-8888'. Esperado: '98888-8888'")

    def test_desatualizado(self):
        resultado_obtido = self.function("88888888")
        self.assertEqual(resultado_obtido,("988888888"), msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Telefone: '88888888'. Esperado: '988888888'")