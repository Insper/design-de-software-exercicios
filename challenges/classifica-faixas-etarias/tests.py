from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def executa_teste(self,
                      arg,
                      esperado,
                      prefixo='Não funcionou para algum teste.'):
        obtido = self.function(arg)
        msg = prefixo + ' Esperado: {0}. Obtido: {1}'.format(esperado, obtido)
        self.assertEqual(
            len(esperado),
            len(obtido),
            msg=msg +
            ' O dicionário obtido não possui a quantidade de itens esperada.')
        for faixa, nomes_esperados in esperado.items():
            nomes_obtidos = obtido[faixa]
            self.assertEqual(
                len(nomes_esperados),
                len(nomes_obtidos),
                msg=msg +
                ' Na faixa {0} foram obtidas quantidades diferentes de nomes ({1} vs. {2})'
                .format(faixa, len(nomes_esperados), len(nomes_obtidos)))
            for nome in nomes_esperados:
                self.assertTrue(
                    nome in nomes_obtidos,
                    msg=msg + ' O nome {0} deveria estar na faixa {1}'.format(
                        nome, faixa))

    def test_1(self):
        self.executa_teste(
            {
                'João': 10,
                'Maria': 8,
                'Miguel': 20,
                'Helena': 67,
                'Alice': 50
            }, {
                'criança': ['João', 'Maria'],
                'adolescente': [],
                'adulto': ['Miguel', 'Alice'],
                'idoso': ['Helena']
            },
            prefixo='Não funcionou para o exemplo do enunciado.')
        testes = [
            ({
                'João': 15,
            }, {
                'criança': [],
                'adolescente': ['João'],
                'adulto': [],
                'idoso': [],
            }),
            ({
                'José': 90,
            }, {
                'criança': [],
                'adolescente': [],
                'adulto': [],
                'idoso': ['José'],
            }),
            ({
                'Frajola': 73,
                'Pateta': 83,
                'Jerry': 75,
                'Willy Coiote': 66,
                'Bob Esponja': 27,
                'Doug Funnie': 11,
                'Arnold': 26,
                'Judy Jetson': 15,
                'Tommy': 1,
                'Docinho': 6,
            }, {
                'criança': ['Docinho', 'Doug Funnie', 'Tommy'],
                'adolescente': ['Judy Jetson'],
                'adulto': ['Arnold', 'Bob Esponja'],
                'idoso': ['Frajola', 'Jerry', 'Pateta', 'Willy Coiote'],
            }),
        ]
        for arg, esperado in testes:
            self.executa_teste(arg, esperado)
