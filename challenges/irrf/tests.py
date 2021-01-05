from strtest import str_test

GABARITO_FAIXAS_INSS = {
    1045: 0.075,
    2089.60: 0.09,
    3134.40: 0.12,
    6101.06: 0.14
}
GABARITO_FAIXAS_IRRF = {
    1903.98: (0, 0),
    2826.65: (0.075, 142.80),
    3751.05: (0.15, 354.8),
    4664.68: (0.225, 636.13),
}


def gabarito_perto(numero, numeros, delta=0.5):
    '''Devolve True se o numero está a menos do que delta de distância de algum dos números da sequência numeros.'''
    for n in numeros:
        if abs(numero - n) <= delta:
            return True
    return False


def gabarito_contribuicao_inss(salario_bruto):
    for maximo, aliquota in GABARITO_FAIXAS_INSS.items():
        if salario_bruto <= maximo:
            return aliquota * salario_bruto
    return 671.12


def gabarito_base_de_calculo(salario_bruto, dependentes):
    return salario_bruto - gabarito_contribuicao_inss(
        salario_bruto) - dependentes * 189.59


def gabarito_calcula_irrf(salario_bruto, dependentes):
    bc = gabarito_base_de_calculo(salario_bruto, dependentes)

    for maximo, valores in GABARITO_FAIXAS_IRRF.items():
        if bc <= maximo:
            aliquota, deducao = valores
            break
    else:
        aliquota = 0.275
        deducao = 869.36

    return bc * aliquota - deducao


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for salario_bruto in range(100, 10001, 100):
            for dependentes in range(4):
                if not gabarito_perto(salario_bruto, GABARITO_FAIXAS_INSS.keys(
                )) and not gabarito_perto(
                        gabarito_base_de_calculo(salario_bruto, dependentes),
                        GABARITO_FAIXAS_IRRF.keys()):
                    args = (salario_bruto, dependentes)
                    # Transformamos em int pois é suficiente que a parte inteira seja igual
                    esperado = gabarito_calcula_irrf(*args)
                    esperado_trocado = gabarito_calcula_irrf(
                        dependentes, salario_bruto)
                    if int(esperado) != int(float('{0:.0f}'.format(
                            esperado))) or int(esperado_trocado) != int(
                                float('{0:.0f}'.format(esperado_trocado))):
                        continue
                    esperado = int(esperado)
                    esperado_trocado = int(esperado_trocado)

                    # Roda o programa
                    self.mock_input.input_list = args
                    self.program()
                    msg = None
                    try:
                        self.assert_printed(esperado_trocado)
                        msg = 'O usuário digita primeiro o salário bruto e depois o número de dependentes. Verifique se você seguiu esta mesma ordem.'
                    except:
                        pass
                    self.assert_printed(esperado, msg=msg)
