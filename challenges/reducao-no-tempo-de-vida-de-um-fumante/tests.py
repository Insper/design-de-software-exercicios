from strtest import str_test

def check_number(string):
    try:
        float(string)
    except ValueError:
        return False
    return True

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for cigarros in range(0, 10):
            for anos in range(0, 50):
                anos_perdidos = anos * 365 * cigarros * 10 / (60 * 24)
                self.mock_input.input_list.append(cigarros)
                self.mock_input.input_list.append(anos)
                self.program()
                obtido = [float(s) for s in self.mock_print.printed[-1].split() if check_number(s)][-1]
                self.assertAlmostEquals(anos_perdidos, obtido, places=3)
