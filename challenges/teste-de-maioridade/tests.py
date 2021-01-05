from strtest import str_test


def gabarito_dos_professores(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    elif idade >= 18:
        return 'Liberado BRASIL'
    else:
        return 'Não está liberado'


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def clean_str(self, s):
        return ''.join(s.split()).lower()

    def test_maioridade(self):
        for idade in range(1, 30):
            resultado_esperado = gabarito_dos_professores(idade)
            resultado_obtido = self.function(idade)
            self.assertEqual(resultado_esperado, resultado_obtido, 'Não funcionou para a idade {0}'.format(idade))
