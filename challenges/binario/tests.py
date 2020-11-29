"""
Consulte a documenta��o do strtest para mais detalhes: https://github.com/Insper/python-string-test-runner

Guia r�pido:
===========
O TestCaseWrapper possui os seguintes atributos:
    - function: fun��o fornecida pelo usu�rio
    - program: fun��o que executa o programa fornecido pelo usu�rio
    - module: arquivo fornecido pelo usu�rio carregado como um m�dulo Python
Asserts �teis:
    - assert_similar(self, string1, string2, dist_max=1, case_sensitive=False, msg=None)
    - assert_printed(self, value, index=None, msg=None)
    - assert_printed_all(self, values, msg=None, **kwargs)
Mocks (todas as fun��es tem os atributos calls, args e kwargs, que guardam a quantidade de chamadas realizadas e os argumentos):
    - mock_print: atributo printed guarda a lista de strings impressas
    - mock_input: atributo input_list recebe uma sequ�ncia de entradas a serem utilizadas
    - mock_open: atributo opened � uma lista de arquivos que n�o foram fechados e � poss�vel adicionar arquivos falsos no dicion�rio files (chave � o nome do arquivo e o valor � o seu conte�do)
    - mock_random: chaves s�o tuplas com os argumentos esperados e valores s�o sequ�ncias de n�meros

Se for implementar os m�todos setUpClass, setUp e tearDown lembre-se de chamar a fun��o da classe m�e.
"""
from strtest import str_test


# O nome da classe deve necessariamente ser TestCase
class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 3  # Limite de tempo em segundos por teste (default: 3s)

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
