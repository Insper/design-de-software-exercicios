from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [{
            'Nico Uno': '01/01/1992',
            'Horácio P. Genaro': '03/03/1992',
            'Ukibe Nokome': '05/05/1992',
            'Maurício Melo': '07/09/1992',
            'Abigail Oliveira': '09/09/1992',
        }]
        esperados = [{'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a string {0}'.format(entrada))
