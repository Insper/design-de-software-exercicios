from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def apply_test(self, month_i):
        months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        month = months[month_i-1]
        self.mock_input.input_list = [month]
        self.program()
        printed = self.mock_print.printed[-1].lower()
        self.assertTrue(str(month_i) in printed, 'Não funcionou para o mês {0}. Esperava "{1}", mas o programa imprimiu "{2}"'.format(month, month_i, printed))

    def test_1(self):
        self.apply_test(1)

    def test_2(self):
        self.apply_test(2)

    def test_3(self):
        self.apply_test(3)

    def test_4(self):
        self.apply_test(4)

    def test_5(self):
        self.apply_test(5)

    def test_6(self):
        self.apply_test(6)

    def test_7(self):
        self.apply_test(7)

    def test_8(self):
        self.apply_test(8)

    def test_9(self):
        self.apply_test(9)

    def test_10(self):
        self.apply_test(10)

    def test_11(self):
        self.apply_test(11)

    def test_12(self):
        self.apply_test(12)
