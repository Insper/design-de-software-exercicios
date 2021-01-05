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

    
    def test_argumentos_zero(self):
        resultado_obtido = self.function('funcionando')
        self.assertEqual('fncnnd', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Palavra teste: "funcionando". Resultado: {resultado_obtido}')

    def test_argumentos_um(self):
        resultado_obtido = self.function('Desoft')
        self.assertEqual('Dsft', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Palavra teste: "Desoft". Resultado: {resultado_obtido}')

    def test_argumentos_dois(self):
            resultado_obtido = self.function('remove vogais')
            self.assertEqual('rmv vgs', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado. Palavra teste: "remove vogais". Resultado: {resultado_obtido}')

    def test_argumentos_vogais(self):
            resultado_obtido = self.function('aeiou')
            self.assertEqual('', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado para uma string de vogais. Palavra teste: "aeiou". Resultado: {resultado_obtido}')

    def test_argumentos_sem_vogais(self):
                resultado_obtido = self.function('Dsft')
                self.assertEqual('Dsft', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado para uma string sem vogais. Palavra teste: "Dsft". Resultado: {resultado_obtido}')

    def test_argumentos_maiusculas(self):
                resultado_obtido = self.function('DESOFT')
                self.assertEqual('DSFT', resultado_obtido, msg=f'O resultado obtido foi diferente do esperado para vogais maiúsculas. Palavra teste: "aeiou". Resultado: {resultado_obtido}')