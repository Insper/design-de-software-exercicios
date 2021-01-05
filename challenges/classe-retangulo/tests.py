from strtest import str_test

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        r = self.module.Retangulo(Ponto(1, 2), Ponto(3, 8))
        self.assertEqual(16, r.calcula_perimetro(), 'Cálculo do perimetro está errado. Pontos testados: (1, 2) e (3, 8)')
        self.assertEqual(12, r.calcula_area(), 'Cálculo da área está errado. Pontos testados: (1, 2) e (3, 8)')
