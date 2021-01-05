from strtest import str_test
from itertools import cycle


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_input.input_list = cycle(
            ['sim', 'talvez', 'ainda um pouco', 'não'])
        self.program()
        self.assertEqual(
            self.mock_input.calls, 4,
            'Número de chamadas para o input foi diferente do esperado')
        self.assertEqual(self.mock_print.calls, 4,
                         'Use exatamente um print por resposta do usuário')
        for i in range(3):
            self.assertTrue('Pratique mais' in self.mock_print.printed[i])
        self.assertTrue('Até a próxima' in self.mock_print.printed[-1])

    def test_de_primeira(self):
        self.mock_input.input_list = cycle(['não'])
        self.program()
        self.assertEqual(
            self.mock_input.calls, 1,
            'Número de chamadas para o input foi diferente do esperado')
        self.assertEqual(self.mock_print.calls, 1,
                         'Use exatamente um print por resposta do usuário')
        self.assertTrue('Até a próxima' in self.mock_print.printed[-1])
