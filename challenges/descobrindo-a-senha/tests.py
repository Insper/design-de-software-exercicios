from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        chutes = ['asdf', '1234', 'senha123', 'desisto']
        self.mock_input.input_list = chutes
        self.program()
        self.assertEqual(self.mock_input.calls, len(chutes))
        self.assertTrue('acertou a senha' in self.mock_print.printed[-1])

    def test_de_primeira(self):
        chutes = ['desisto']
        self.mock_input.input_list = chutes
        self.program()
        self.assertEqual(self.mock_input.calls, len(chutes))
        self.assertTrue('acertou a senha' in self.mock_print.printed[-1])
