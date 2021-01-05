from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        telefones_raw = [
            '+5511912345678',
            '1155556666',
            '77778888',
            '+551133334444',
            '918273645',
            '11987654321',
            '+551931423546',
            '+5521932435465',
            '3132435465',
            '41934234345',
            '87432389',
            '923345466',
        ]
        esperado = {
            '+5511912345678': '912345678',
            '918273645': '918273645',
            '11987654321': '987654321',
            '+5521932435465': '932435465',
            '41934234345': '934234345',
            '923345466': '923345466',
        }
        obtido = self.function(telefones_raw)
        self.assertIsNotNone(obtido, msg='Não foi obtida resposta. Você não se esqueceu do return?')
        for tel in obtido:
            self.assertEqual(9, len(tel), msg='Telefone no formato errado. Todos os telefones na lista devolvida devem conter exatamente 9 dígitos. Obtido: {0}'.format(tel))
        for raw_cel, cel in esperado.items():
            self.assertIn(cel, obtido, msg='O número {0} é um telefone celular, mas o número {1} não está na lista devolvida pela função.'.format(raw_cel, cel))
        self.assertEqual(len(esperado), len(obtido), msg='A quantidade de números de telefone na lista devolvida é diferente do esperado. Não funcionou para a lista {0}. Obtido: {1}'.format(telefones_raw, obtido))
