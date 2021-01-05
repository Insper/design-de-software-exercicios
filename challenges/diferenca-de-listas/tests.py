'''
Faça uma função que recebe 2 listas e retorna uma nova lista com os elementos da primeira lista que não estão na segunda lista.

Exemplo: para a entrada `lista1 = [2, 7, 3.1, 'banana']` e `lista2 = [2, 'banana', 'carro']` sua função deve devolver a lista `[7, 3.1]`.

Atenção, esse é só um exemplo, sua função deve conseguir lidar com quaisquer listas de entrada e não apenas com as do exemplo.

Nome da função: subtracao_de_listas
'''

from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Não funcionou para duas listas vazias.')
    def test_duas_listas_vazias(self):
        sub = self.function([], [])
        self.assertEqual(0, len(sub))

    @str_test.error_message(
        'Não funcionou quando a primeira lista é vazia e a segunda não.')
    def test_primeira_lista_vazia(self):
        sub = self.function([], [1, 2, 3])
        self.assertEqual(0, len(sub))

    @str_test.error_message(
        'Não funcionou quando a segunda lista é vazia e a primeira não.')
    def test_segunda_lista_vazia(self):
        sub = self.function([1, 2, 3], [])
        self.assertEqual(3, len(sub))
        self.assertTrue(1 in sub)
        self.assertTrue(2 in sub)
        self.assertTrue(3 in sub)

    @str_test.error_message('Não funcionou para o exemplo do enunciado.')
    def test_exemplo_enunciado(self):
        sub = self.function([2, 7, 3.1, 'banana'], [2, 'banana', 'carro'])
        self.assertEqual(2, len(sub))
        self.assertTrue(7 in sub)
        self.assertTrue(3.1 in sub)
