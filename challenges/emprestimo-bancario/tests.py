from strtest import str_test


def gabarito_dos_professores(valor, salario, anos):
    parcela = valor / (anos * 12)
    if parcela > salario * 0.3:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for valor in range(0, 100000, 10000):
            for salario in range(500, 1000, 100):
                for anos in range(1, 50, 5):
                    resposta = gabarito_dos_professores(valor, salario, anos)
                    self.mock_input.input_list.append(valor)
                    self.mock_input.input_list.append(salario)
                    self.mock_input.input_list.append(anos)
                    self.program()
                    self.assertTrue(resposta.lower() in self.mock_print.printed[-1].lower())
