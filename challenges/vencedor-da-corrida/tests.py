from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        esperados = [{
            'Nico Uno': 4.472,
            'Horácio P. Genaro': 3.651,
            'Ukibe Nokome': 8.165,
            'Maurício Melo': 3.162,
            'Abigail Oliveira': 3.430,
        }]
        self.mock_input.input_list = ['Nico Uno', '10', 'Horácio P. Genaro', '15', 'Ukibe Nokome', '3', 'Maurício Melo', '20', 'Abigail Oliveira', '17', 'sair']
        self.program()
        self.assertTrue('Maurício Melo' in self.mock_print.printed[-1])
        self.assertTrue('3.1' in self.mock_print.printed[-1])
