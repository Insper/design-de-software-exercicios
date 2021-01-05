from strtest import str_test
import numbers


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [
            (('luciop', ['andrek', 'fabio']), 'luciop'),
            (('luciop', ['andrek', 'fabio', 'luciop']), 'luciop1'),
            (('luciop', ['andrek', 'fabio', 'luciop', 'luciop1']), 'luciop2'),
            (('andre', ['andrek', 'fabio', 'luciop', 'luciop1']), 'andre'),
            (('andrek', ['andrek', 'fabio', 'luciop', 'luciop1']), 'andrek1'),
        ]
        for args, esperado in entradas:
            obtido = self.function(*args)
            msg = 'Não funcionou para os argumentos {0} e {1} (passados nesta ordem). Esperado={2}. Obtido={3}'.format(
                args[0], args[1], esperado, obtido)
            if obtido is None:
                msg += ' Será que você não se esqueceu do return?'
            elif not isinstance(obtido, str):
                msg += ' Era esperado que sua função retornasse uma string, mas ela retornou algo diferente.'
            self.assertEqual(esperado, obtido, msg=msg)
