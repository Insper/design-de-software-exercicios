from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        c = self.module.Carrinho()
        c.adiciona('banana', 5)
        t = c.total_do_produto('banana')
        self.assertEqual(5, t, msg='Não funcionou para a primeira chamada do total_do_produto do enunciado. Esperado: 5. Obtido: {0}'.format(t))
        c.adiciona('abacate', 7)
        c.adiciona('banana', 4)
        t = c.total_do_produto('banana')
        self.assertEqual(9, t, msg='Não funcionou para a segunda chamada do total_do_produto do enunciado. Esperado: 9. Obtido: {0}'.format(t))
        t = c.total_do_produto('abacate')
        self.assertEqual(7, t, msg='Não funcionou para o preço do abacate do enunciado. Esperado: 7. Obtido: {0}'.format(t))
