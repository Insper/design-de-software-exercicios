from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        respostas = [(4, 1030110641), (0, 234587543839457), (1, 1), (2, 987654321123456789)]
        for esperada, entrada in respostas:
            resposta = self.function(entrada)
            self.assertEqual(esperada, resposta, 'Não funcionou para o número {0}'.format(entrada))
