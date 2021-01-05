from strtest import str_test


def c_(t):
    codigos = dict(zip('zebras', 'zebras'[::-1]))
    return ''.join(codigos.get(c, c) for c in t)


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        textos = ['''milho de pipoca que nao passa pelo fogo continua a ser milho de pipoca, para sempre.
assim acontece com a gente.
as grandes transformacoes acontecem quando passamos pelo fogo.
quem nao passa pelo fogo fica do mesmo jeito, a vida inteira.
rubem alves''', '''bancos futeis pagavam-lhe queijo, whisky e xadrez.
um pequeno jabuti xereta viu dez cegonhas felizes.
como uma zebra numa manada de ovelhas.''']
        for texto in textos:
            self.mock_open.files['criptografado.txt'] = c_(texto)
            self.program()
            msg = 'Resposta incorreta. Verifique a saída do terminal.'
            for linha in texto.splitlines():
                self.assert_printed(linha, msg=msg)
