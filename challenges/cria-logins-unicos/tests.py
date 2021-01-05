from strtest import str_test
import numbers


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [
            (('andrek', 'fabio', 'luciop', 'fim'), ('andrek', 'fabio', 'luciop')),
            (('andrek', 'luciop', 'fabio', 'luciop', 'fim'), ('andrek', 'luciop', 'fabio', 'luciop1')),
            (('andrek', 'luciop', 'fabio', 'luciop', 'luciop', 'luciop', 'fim'), ('andrek', 'luciop', 'fabio', 'luciop1', 'luciop2', 'luciop3')),
            (('andrek', 'fabio', 'luciop', 'luciop', 'andre', 'fim'), ('andrek', 'fabio', 'luciop', 'luciop1', 'andre')),
            (('andrek', 'fabio', 'luciop', 'luciop', 'andrek', 'fim'), ('andrek', 'fabio', 'luciop', 'luciop1', 'andrek1')),
        ]
        for inputs, outputs in entradas:
            self.mock_input.input_list = inputs
            self.program()
            msg = 'Não funcionou para os inputs {0} (passados nesta ordem). Verifique a saída no terminal.'.format(
                ','.join("'{0}'".format(i) for i in inputs))
            for out in outputs:
                self.assert_printed(out, msg=msg)
            imprimiu_fim = False
            try:
                self.assert_printed('fim')
                imprimiu_fim = True
            except:
                pass
            if imprimiu_fim:
                self.fail('Não deveria ter dado print na string "fim"')
