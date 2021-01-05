from strtest import str_test


TEXTO = '''
Um texto contendo algumas palavras mas nenhuma pontuação
Existem algumas linhas com texto e banana e outras

sem nada
Existem muitos tipos de BANANA

Banana nanica banana da terra
Banana ouro
Banana prata
Banana maçã

E várias outras
Será que você pegou todas?
'''


def gabarito():
    t = TEXTO.replace('\n', ' ').lower()
    return sum(1 for w in t.split() if w == 'banana')


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_write(self):
        self.mock_open.files['macacos-me-mordam.txt'] = TEXTO
        self.program()
        self.assertEqual(self.mock_open.calls, 1)
        self.assertEqual(len(self.mock_open.opened), 0)
        self.assertTrue(str(gabarito()) in self.mock_print.printed[0])
