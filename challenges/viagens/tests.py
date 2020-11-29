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
        
        destinos={
        "Miami":[1,1000],
        "Ilhas Sandwich do Sul":[4,5000],
        "Barcelona":[2, 2000],
        "Osasco":[5,200],
        "Buenos Aires":[3,500]
        }

        destinos_promocao={
         'Miami': 900.0,
         'Ilhas Sandwich do Sul': 3000.0, 
         'Barcelona': 1600.0, 
         'Osasco': 100.0, 
         'Buenos Aires': 350.0}

        resultado_obtido = self.function(destinos)
        self.assertDictEqual(destinos_promocao, resultado_obtido, msg=f'A função não devolveu o resultado esperado para o dicionário {destinos}')
        
    def test_2(self):
        
        destinos2={
        "Galápagos":[1,12000],
        "Hum":[4,3750],
        "Melbourne":[2, 6235],
        "Juneau":[5,2200],
        "Chicago":[3,780]
        }

        destinos_promocao2={'Galápagos': 10800.0, 
        'Hum': 2250.0, 
        'Melbourne': 4988.0, 
        'Juneau': 1100.0, 
        'Chicago': 546.0}

        resultado_obtido = self.function(destinos2)
        self.assertDictEqual(destinos_promocao2, resultado_obtido, msg=f'A função não devolveu o resultado esperado para o dicionário {destinos2}')
        