from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        testes = [
            ([
                {'nome': ' Michael Phelps', 'nacionalidade': 'Norte Americano', 'ouro': 23, 'prata': 3, 'bronze': 2,},
                {'nome': 'Larisa Latynina', 'nacionalidade': 'Russo', 'ouro': 9, 'prata': 5, 'bronze': 4,},
                {'nome': 'Nikolai Andrianov', 'nacionalidade': 'Russo', 'ouro': 7, 'prata': 5, 'bronze': 3,},
                {'nome': 'Boris Shakhlin', 'nacionalidade': 'Russo', 'ouro': 7, 'prata': 4, 'bronze': 2,},
                {'nome': 'Jenny Thompson', 'nacionalidade': 'Norte Americano', 'ouro': 8, 'prata': 3, 'bronze': 1,}
            ], 'Norte Americano'),
            ([
                {"nome": "Fulano", "nacionalidade": "brasileiro", "ouro": 2, "prata": 0, "bronze": 0},
                {"nome": "Beltrano", "nacionalidade": "paraguaio", "ouro": 1, "prata": 1, "bronze": 1},
                {"nome": "Ciclano", "nacionalidade": "brasileiro", "ouro": 0, "prata": 0, "bronze": 1}
            ], 'brasileiro')
        ]
        for teste, esperado in testes:
            obtido = self.function(teste)
            self.assertIsNotNone(obtido, msg='Nenhum valor devolvido. Você não se esqueceu do return?')
            self.assertTrue(isinstance(obtido, str), msg='O valor devolvido não é uma string. Era esperada a nacionalidade com mais medalhas de ouro. Obtido: {0}'.format(obtido))
            self.assertEqual(esperado, obtido, msg='Não funcionou para a lista {0}. Esperado: {1}. Obtido: {2}'.format(teste, esperado, obtido))
