from strtest import str_test
import numbers


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [
            ({
                "São Paulo": {
                    "São Paulo": 21571281,
                    "Campinas": 3224443,
                },
                "Minas Gerais": {
                    "Belo Horizonte": 2385639,
                    "Uberlândia": 611903,
                },
            }, "São Paulo"),
            ({
                "São Paulo": {
                    "São Paulo": 385639,
                    "Campinas": 11903,
                },
                "Minas Gerais": {
                    "Belo Horizonte": 1571281,
                    "Uberlândia": 224443,
                },
            }, "Minas Gerais"),
            ({
                "Distrito Federal": {
                    "Brasília": 3015268,
                },
                "Bahia": {
                    "Salvador": 2872347,
                    "Feira de Santana": 614872,
                    "Vitória da Conquista": 341597,
                },
                "Rio de Janeiro": {
                    "Rio de Janeiro": 6718903,
                    "São Gonçalo": 1084839,
                    "Duque de Caxias": 919596,
                },
                "Amazonas": {
                    "Manaus": 2182763,
                    "Parintins": 114273,
                    "Itacoatiara": 101337,
                },
            }, "Rio de Janeiro"),
        ]
        for estados, esperado in entradas:
            obtido = self.function(estados)
            msg = 'Não funcionou para o dicionário {0}. Esperado={1}. Obtido={2}'.format(
                estados, esperado, obtido)
            if obtido is None:
                msg += ' Será que você não se esqueceu do return?'
            elif isinstance(obtido, numbers.Number):
                msg += ' Será que você não retornou o tamanho da população ao invés do nome do estado?'
            elif not isinstance(obtido, str):
                msg += ' Era esperado que sua função retornasse uma string, mas ela retornou algo diferente.'
            self.assertEqual(esperado, obtido, msg=msg)
