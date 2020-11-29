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

    def test_data_certa(self):
        resultado_obtido = self.function('20/08/2020')
        self.assertTrue(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 20/08/2020 é válida.')

    def test_dia_errado(self):
        resultado_obtido = self.function("40/08/2020")
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 40/08/2020 não é válida.')

    def test_fevereiro(self):
        resultado_obtido = self.function("30/02/2019")
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 30/02/2020 não é válida.')

    def test_bissexto_true(self):
        resultado_obtido = self.function("29/02/2020")
        self.assertTrue(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 29/02/2020 é válida (ano bissexto a cada 4).')

    def test_bissexto_false(self):
        resultado_obtido = self.function("29/02/2019")
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 29/02/2019 não é válida (ano bissexto a cada 4).')

    def test_mes_false(self):
        resultado_obtido = self.function("02/80/2020")
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 02/80/2020 não é válida.')

    def test_mes_30(self):
        resultado_obtido = self.function("31/04/2020")
        self.assertFalse(resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. A data 31/04/2020 não é válida(lembre-se que alguns meses possuem apenas 30 dias!).')