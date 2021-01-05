from strtest import str_test

POEMA = '''Minha terra tem palmeiras
Onde canta o Sabiá
As aves que aqui gorjeiam
Não gorjeiam como lá
'''


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_open.files['texto.txt'] = POEMA
        self.program()
        self.assertEqual(len(self.mock_open.opened),
                         0,
                         msg='Você se esqueceu de fechar o arquivo!')
        self.assert_printed(
            17,
            msg='Não funcionou para o arquivo que contém o seguinte texto: "{0}"'
            .format(POEMA))
