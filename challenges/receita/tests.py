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
        receita = {
        "ovos":"4",
        "açúcar":"2 xícaras",
        "leite":"1 xícara",
        "farinha":"2 xícaras",
        "fermento": "1 colher de sopa",
        "baunilha":"1 colher de chá"
        }
        receita_convertida = {
            'ovos': '4', 
            'açúcar': '500 ml', 
            'leite': '250 ml', 
            'farinha': '500 ml', 
            'fermento': '15 ml', 
            'baunilha': '5 ml'
            }
        resultado_obtido = self.function(receita)
        self.assertDictEqual(receita_convertida, resultado_obtido, msg=f'A função não devolveu o resultado esperado para o dicionário {receita}')
        
    def test_2(self):

        receita2 = {
        "ovos":"3",
        "leite":"2 xícaras",
        "óleo":"1 xícara",
        "farinha":"3 xícaras",
        "fermento": "1 colher de sopa",
        "sal":"2 colheres de chá"
        }
        receita_convertida2 = {
        'ovos': '3',
        'leite': '500 ml',
        'óleo': '250 ml',
        'farinha': '750 ml',
        'fermento': '15 ml',
        'sal': '10 ml'
        }
        resultado_obtido = self.function(receita2)
        self.assertDictEqual(receita_convertida2, resultado_obtido, msg=f'A função não devolveu o resultado esperado para o dicionário {receita2}')
        
        