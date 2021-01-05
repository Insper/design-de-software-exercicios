from strtest import str_test

def gabarito_dos_professores(salario_atual):
    if salario_atual > 1250:
        return salario_atual * 0.1
    else:
        return salario_atual * 0.15


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Não funcionou para algum salário')
    def test_1(self):
        for salario in range(1000, 2000):
            aumento = gabarito_dos_professores(salario)
            self.assertAlmostEquals(aumento, self.function(salario), places=3)
