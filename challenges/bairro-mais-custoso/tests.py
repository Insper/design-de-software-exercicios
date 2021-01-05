from strtest import str_test
import numbers


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [
            {
                'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
                'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
                'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
            },
            {
                'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
                'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
                'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
                'Bairro 4': [51312.21, 5234.64, 23463.67, 6347.12, 2458.61, 8452.25, 7234.23, 7234.34, 7341.21, 31246.43, 2136.12, 2347.64],
                'Bairro 5': [24578.32, 23475.45, 2458.56, 7452.34, 3485.87, 24578.21, 7345.74, 12347.34, 8245.43, 23457.41, 8453.12, 3458.75],
            },
            {
                'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
            },
        ]
        for bairros in entradas:
            custos = {b: sum(c[-6:]) for b, c in bairros.items()}
            esperado = max(custos.items(), key=lambda x: x[1])[0]
            obtido = self.function(bairros)
            msg = 'Não funcionou para o dicionário {0}. Esperado={1}. Obtido={2}'.format(
                bairros, esperado, obtido)
            if obtido is None:
                msg += ' Será que você não se esqueceu do return?'
            elif isinstance(obtido, numbers.Number):
                msg += ' Será que você não retornou o custo total ao invés do nome do bairro?'
            elif isinstance(obtido, dict):
                msg += ' Será que você não retornou o dicionário inteiro ao invés do nome do bairro?'
            elif not isinstance(obtido, str):
                msg += ' Era esperado que sua função retornasse uma string (nome do bairro), mas ela retornou algo diferente.'
            self.assertEqual(esperado, obtido, msg=msg)
