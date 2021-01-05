from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def clean_str(self, s):
        return ''.join(s.split()).lower()

    @str_test.error_message('Não funcionou para algum teste. Uma possibilidade é um erro no formato do texto. Verifique se todos os caracteres estão corretos.')
    def test_print_called(self):
        self.mock_input.input_list = ['9.99']
        self.program()
        self.assertEqual(self.mock_input.calls, 1)
        self.assertEqual(self.mock_print.calls, 1)
        self.assertEqual(self.clean_str(self.mock_print.printed[0]), self.clean_str('Valor da conta com 10%: R$ 10.99'))
