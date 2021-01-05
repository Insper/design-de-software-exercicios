from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def total_segundos(self, dias, horas, minutos, segundos):
        return segundos + 60 * (minutos + 60 * (horas + 24 * dias))

    def test_1(self):
        args = [3, 5, 19, 37]  # dias, horas, minutos, segundos
        self.mock_input.input_list = [str(i) for i in args]
        self.program()
        self.assertEqual(self.mock_input.calls, len(args), 'Deveria chamar o input {0} vezes'.format(len(args)))
        self.assertEqual(self.mock_print.calls, 1, 'Deveria chamar o print somente uma vez')
        self.assertTrue(str(self.total_segundos(*args)) in self.mock_print.printed[0])
