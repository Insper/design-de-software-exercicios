from strtest import str_test


def gabarito_dos_professores(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    d = 3
    while d < n/2:
        if n % d == 0:
            return False
        d += 2
    return True


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        for n in range(200):
            self.assertEqual(gabarito_dos_professores(n), self.function(n), 'NÃ£o funcionou para o nÃºmero {0}'.format(n))