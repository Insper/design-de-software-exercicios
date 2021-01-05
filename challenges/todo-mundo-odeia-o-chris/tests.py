from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_print_called(self):
        self.mock_input.input_list = ['Mundo']
        self.program()
        self.assertEqual(
            self.mock_input.calls, 1,
            'Mais do que um input foi utilizado. Era esperado apenas uma chamada do input.'
        )
        self.assertEqual(
            self.mock_print.calls, 1,
            'Mais do que um print foi utilizado. Era esperado apenas uma chamada do print.'
        )
        self.assert_printed('Olá, Mundo')

    def test_hello_world(self):
        self.mock_input.input_list = ['Chris']
        self.program()
        self.assertEqual(
            self.mock_input.calls, 1,
            'Mais do que um input foi utilizado. Era esperado apenas uma chamada do input.'
        )
        self.assertEqual(
            self.mock_print.calls, 1,
            'Mais do que um print foi utilizado. Era esperado apenas uma chamada do print.'
        )
        self.assert_printed('Todo mundo odeia o Chris')
