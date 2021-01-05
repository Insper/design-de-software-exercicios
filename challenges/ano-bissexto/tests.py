from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def clean_str(self, s):
        return ''.join(s.split()).lower()

    def test_bissexto(self):
        for ano in range(1, 2050):
            if ano % 4 != 0:
                resultado_esperado = False
            elif ano % 400 == 0:
                resultado_esperado = True
            elif ano % 100 == 0:
                resultado_esperado = False
            else:
                resultado_esperado = True

            resultado_obtido = self.function(ano)
            self.assertEqual(resultado_esperado, resultado_obtido, 'Não funcionou para o ano {0}'.format(ano))
