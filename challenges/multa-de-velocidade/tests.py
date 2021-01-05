from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for velocidade in range(0, 120):
            multa = '{0:.2f}'.format((velocidade - 80) * 5)
            self.mock_input.input_list.append(velocidade)
            self.program()
            if velocidade > 80:
                self.assertTrue(multa in self.mock_print.printed[-1])
            else:
                self.assertTrue(multa not in self.mock_print.printed[-1])
