from strtest import str_test

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        c = self.module.Circulo(Ponto(10, 25), 5)
        self.assertTrue(c.contem(Ponto(10, 25)), 'O circulo deve conter seu próprio centro.')
        self.assertTrue(c.contem(Ponto(12, 28)), 'Não funcionou para um ponto dentro do circulo.')
        self.assertFalse(c.contem(Ponto(14, 29)), 'Não funcionou para um ponto fora do circulo.')
        self.assertFalse(c.contem(Ponto(-100, -30)), 'Não funcionou para um ponto fora do circulo.')
