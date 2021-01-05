from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [
            ('banana', ('ban***', None)),
            ('abacaxi', ('ab*c*xi', None)),
            ('Um mago nunca se atrasa, nem se adianta, ele chega exatamente quando pretende chegar',
            ('Um *ago*nu*c**se**tr***,*********di*******l***h*****x*********q******p**************',
            'Um *ago*n**c**se**tr***,*********di*******l***h*****x*********q******p**************')),
            ('AaAabBbB', ('Aa**bB**', 'A***b***')),
        ]
        for arg, esperados in entradas:
            obtido = self.function(arg)

            msg = 'Não funcionou para "{0}". Esperado="{1}". Obtido="{2}".'.format(arg, esperados[0], obtido)
            self.assertIn(obtido, esperados, msg=msg)
