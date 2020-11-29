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

    def test_argumentos_normal(self):
        resultado_obtido = self.function("frase pra testar se a função filtra as palavaras",5)
        self.assertListEqual(resultado_obtido,(['testar', 'função', 'filtra', 'palavaras']), msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Frase de teste: 'frase pra testar se a função filtra as palavaras'. Tamanho mínimo:5. Esperado: ['testar', 'função', 'filtra', 'palavaras']")

    def test_argumentos_maiusculo(self):
            resultado_obtido = self.function("STRING DE PALAVRAS MAIÚSCULAS",4)
            self.assertListEqual(resultado_obtido,['STRING', 'PALAVRAS', 'MAIÚSCULAS'], msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Expressão de teste: 'STRING DE PALAVRAS MAIÚSCULAS'. Tamanho mínimo:4. Esperado: ['STRING', 'PALAVRAS', 'MAIÚSCULAS']")
    
    def test_argumentos_longo(self):
            resultado_obtido = self.function("Deve devolver todas as Palavras",1)
            self.assertListEqual(resultado_obtido,['Deve', 'devolver', 'todas', 'as', 'Palavras'], msg=f"O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Frase de teste: 'Deve devolver todas as Palavras'. Tamanho mínimo:1. Esperado:['Deve', 'devolver', 'todas', 'as', 'Palavras']")
    
    def test_argumentos_curto(self):
            resultado_obtido = self.function("oi",3)
            self.assertCountEqual(resultado_obtido,[], msg=f'O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Palavra de teste: "oi". Tamanho mínimo:3. Esperado: []')
    
    def test_argumentos_vazio(self):
            resultado_obtido = self.function("",3)
            self.assertCountEqual(resultado_obtido,[], msg=f'O resultado obtido foi diferente do esperado. Obtido: {resultado_obtido}. Palavra de teste: "". Tamanho mínimo:3. Esperado: []')
    