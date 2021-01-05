from strtest import str_test


def eh_primo_gabarito(n):
    if n == 2:
        return True
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    d = 3
    while d < n:
        if n % d == 0:
            return False
        d += 2
    return True


def gabarito_dos_professores(n):
    encontrados = 0
    i = 2
    primos = []
    while encontrados < n:
        if eh_primo_gabarito(i):
            primos.append(i)
            encontrados += 1
        i += 1
    return primos


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        n = 100
        primos = gabarito_dos_professores(n)
        retval = self.function(n)
        self.assertEqual(n, len(retval), 'Deveria ter exatamente n números primos')
        for primo, returned in zip(primos, retval):
            self.assertEqual(primo, returned, 'Não retornou os n primeiros primeos em ordem crescente')
