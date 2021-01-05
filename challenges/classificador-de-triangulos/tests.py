from strtest import str_test


def gabarito_dos_professores(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return 'equilátero'
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return 'isósceles'
    else:
        return 'escaleno'

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def clean_str(self, s):
        return ''.join(s.split()).lower()

    def test_1(self):
        for l1 in range(1, 20):
            for l2 in range(1, 20):
                for l3 in range(1, 20):
                    resultado_esperado = gabarito_dos_professores(l1, l2, l3).lower()
                    resultado_obtido = self.function(l1, l2, l3).lower()
                    self.assertEqual(resultado_esperado, resultado_obtido, 'Não funcionou para os lados {0}, {1}, {2}'.format(l1, l2, l3))
