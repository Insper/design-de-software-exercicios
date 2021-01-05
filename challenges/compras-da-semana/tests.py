from strtest import str_test


_BOLO_DE_CHOCOLATE = 'Bolo de chocolate'
_BOLINHO_DE_CHUVA = 'Bolinho de chuva'
_MINGAU = 'Mingau'


def _bolo_de_chocolate():
    return {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    }


def _bolinho_de_chuva():
    return {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    }


def _mingau():
    return {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }


_RECEITA_FACTORY = {
    _BOLO_DE_CHOCOLATE: _bolo_de_chocolate,
    _BOLINHO_DE_CHUVA: _bolinho_de_chuva,
    _MINGAU: _mingau,
}


def _cria_receitas(*receitas):
    return {receita: _RECEITA_FACTORY[receita]() for receita in receitas}


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        testes = (
            (_cria_receitas(_BOLO_DE_CHOCOLATE, _BOLINHO_DE_CHUVA, _MINGAU), [_BOLINHO_DE_CHUVA, _BOLO_DE_CHOCOLATE, _BOLINHO_DE_CHUVA]),
            (_cria_receitas(_BOLO_DE_CHOCOLATE, _MINGAU), [_MINGAU]),
            (_cria_receitas(_BOLINHO_DE_CHUVA), [_BOLINHO_DE_CHUVA, _BOLINHO_DE_CHUVA, _BOLINHO_DE_CHUVA]),
            (_cria_receitas(_BOLO_DE_CHOCOLATE, _BOLINHO_DE_CHUVA, _MINGAU), [_BOLINHO_DE_CHUVA, _BOLO_DE_CHOCOLATE, _BOLINHO_DE_CHUVA, _MINGAU, _MINGAU]),
        )

        for receitas, lista in testes:
            obtido = self.function(receitas, lista)
            ingredientes = set((ingrediente for receita in lista for ingrediente in receitas[receita].keys()))
            esperado = {ingrediente: sum(receitas[receita].get(ingrediente, 0) for receita in lista) for ingrediente in ingredientes}

            msg = f'Não funcionou para a as receitas {receitas} e a lista de pratos {lista}. Resultado obtido={obtido}. Resultado esperado={esperado}.'

            for ingrediente, qtd_esperada in esperado.items():
                self.assertIn(ingrediente, obtido, msg=msg + f' Não encontrei o ingrediente {ingrediente} na sua resposta.')
                qtd_obtida = obtido[ingrediente]
                self.assertAlmostEqual(qtd_obtida, qtd_esperada, msg=msg + f' Quantidade obtida para o igrediente {ingrediente}={qtd_obtida}. Quantidade esperada={qtd_esperada}.')

            for ingrediente in obtido:
                self.assertIn(ingrediente, esperado, msg=msg + f' O ingrediente {ingrediente} não deveria estar na resposta.')
