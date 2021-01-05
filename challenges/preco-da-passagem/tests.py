from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_input.input_list = ['150']
        self.program()
        self.assertEqual(self.mock_input.calls, 1, 'Deveria chamar o input somente uma vez')
        self.assertEqual(self.mock_print.calls, 1, 'Deveria chamar o print somente uma vez')
        self.assertTrue('75.00' in self.mock_print.printed[0])

    def test_2(self):
        self.mock_input.input_list = ['301']
        self.program()
        self.assertEqual(self.mock_input.calls, 1, 'Deveria chamar o input somente uma vez')
        self.assertEqual(self.mock_print.calls, 1, 'Deveria chamar o print somente uma vez')
        self.assertTrue('145.45' in self.mock_print.printed[0])
