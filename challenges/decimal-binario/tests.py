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

    def test_com_zero(self):
        try:
                resultado_obtido = int(self.function(0))
                self.assertEqual(0, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 0. Obtido: {resultado_obtido}')
        except ValueError:
                print("A função devolveu uma string que não pode ser convertida em inteiro.")
    
    def test_argumentos_zero(self):
        try:
                resultado_obtido = int(self.function(10))
                self.assertEqual(1010, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 1010. Obtido: {resultado_obtido}')
        except ValueError:
                print(f"A função devolveu uma string que não pode ser convertida em inteiro.")
    
    def test_argumentos_um(self):
        try:
            resultado_obtido = int(self.function(1))
            self.assertEqual(1, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 1. Obtido: {resultado_obtido}')
        except ValueError:
                print(f"A função devolveu uma string que não pode ser convertida em inteiro.")
    
    def test_argumentos_dois(self):
            resultado_obtido = (self.function(-1))
            self.assertEqual(f"Negativo", resultado_obtido, msg=f'Não funcionou para números negativos. Lembre-se de que a função deve devolver a mensagem "Negativo" nestes casos!')

    def test_argumentos_tres(self):
        try:
                resultado_obtido = int(self.function(11))
                self.assertEqual(1011, resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Esperado: 1011. Obtido: {resultado_obtido}')
        except ValueError:
                print(f"A função devolveu uma string que não pode ser convertida em inteiro.")
    