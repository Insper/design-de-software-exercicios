from strtest import str_test

CHURRAS = '''Água com gás,32,2.54
Carvão,4,11.56
Salsicha,3,18.75
Espeto de frango,5,13.43
Maminha,2,82.40'''


def custo_total():
    total = 0
    for linha in CHURRAS.split('\n'):
        dados = linha.split(',')
        if len(dados) == 3:
            nome, qtd, preco = dados
            total += float(preco) * float(qtd)
    return total


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_open.files['churras.txt'] = CHURRAS
        self.program()
        self.assertEqual(len(self.mock_open.opened), 0)
        self.assertTrue(str(custo_total()) in self.mock_print.printed[-1])
