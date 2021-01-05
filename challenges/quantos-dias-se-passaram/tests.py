from strtest import str_test
from itertools import cycle


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mes = 1
        dia_do_mes = 1
        for dia_do_ano, ano in zip(range(365), cycle((2018, 2019, 2021))):
            data = f'{dia_do_mes:02d}/{mes:02d}/{ano:04d}'
            obtido = self.function(data)
            msg = f'Não funcionou para a data {data}. Esperado={dia_do_ano}. Obtido={obtido}.'
            self.assertEqual(dia_do_ano, obtido, msg=msg)
            if dia_do_mes == dias_por_mes[mes-1]:
                mes += 1
                dia_do_mes = 1
            else:
                dia_do_mes += 1
