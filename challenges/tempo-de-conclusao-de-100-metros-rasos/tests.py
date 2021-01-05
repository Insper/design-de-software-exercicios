from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [{
            'Nico Uno': 10,
            'Horácio P. Genaro': 15,
            'Ukibe Nokome': 3,
            'Maurício Melo': 20,
            'Abigail Oliveira': 17,
        }]
        esperados = [{
            'Nico Uno': 4.472,
            'Horácio P. Genaro': 3.651,
            'Ukibe Nokome': 8.165,
            'Maurício Melo': 3.162,
            'Abigail Oliveira': 3.430,
        }]
        for entrada, esperado in zip(entradas, esperados):
            recebido = self.function(entrada)
            for nome, tempo in esperado.items():
                self.assertTrue(abs(tempo-recebido[nome]) < 0.01, 'Não funcionou para a aceleração {0}'.format(entrada[nome]))
