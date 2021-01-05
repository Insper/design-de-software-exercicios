from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_input.input_list = list(range(10))[::-1]
        self.program()
        self.assertEqual(len(self.mock_input.input_list), self.mock_input.calls)
        self.assertTrue(str(sum(self.mock_input.input_list)) in self.mock_print.printed[-1])

    def test_de_primeira(self):
        self.mock_input.input_list = list(range(10))
        self.program()
        self.assertEqual(1, self.mock_input.calls, 'Deveria chamar input uma única vez se o primeiro número for zero')
        self.assertTrue('0' in self.mock_print.printed[-1])
