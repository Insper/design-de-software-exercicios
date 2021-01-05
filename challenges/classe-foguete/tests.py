from numbers import Number
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        self.assertTrue(hasattr(self.module, 'Foguete'), msg='Não encontrei a classe Foguete. Verifique se digitou o nome corretamente.')
        try:
            foguete = self.module.Foguete(10000)
        except TypeError as e:
            if '2 were given' in str(e):
                self.assertTrue(False, msg='Número de argumentos do __init__ está incorreto. Deveria receber dois argumentos (incluindo o self).')
            else:
                raise e
        self.assertTrue(hasattr(foguete, 'atualizar'), msg='Não encontrei o método atualizar na classe Foguete. Verifique se digitou o nome corretamente e se colocou a definição da função no lugar certo.')
        p = foguete.atualizar(9)
        self.assertIsNotNone(p, msg='Nenhum resultado devolvido pelo método atualizar. Você não se esqueceu do return?')
        msg = 'Não funcionou para o teste do enunciado. Esperado: {0}. Obtido: {1}.'
        if abs(p - 90000) < 1:
            msg += ' Dica: o tempo fornecido para o método atualizar está em segundos.'
        self.assertAlmostEqual(25, p, msg=msg.format(25, p))
        p = foguete.atualizar(18)
        self.assertAlmostEqual(75, p, msg=msg.format(75, p))

        outro_foguete = self.module.Foguete(500)
        p = outro_foguete.atualizar(3600)
        self.assertAlmostEqual(500, p, msg='Não funcionou quando mais do que um foguete é criado. No teste, o novo foguete com velocidade inicial 500 km/h é atualizado com 3600 segundos. Será que você está utilizando alguma variável global? Esperado: {0}. Obtido: {1}'.format(500, p))

        p = foguete.atualizar(9)
        self.assertAlmostEqual(100, p, msg='Não funcionou quando mais do que um foguete é criado. Será que você está utilizando alguma variável global? Esperado: {0}. Obtido: {1}'.format(100, p))
