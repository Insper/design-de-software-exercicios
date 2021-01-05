from strtest import str_test
import json


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        produtos = {
            "produtos": [{
                "produto": "açúcar",
                "quantidade": 4,
                "valor": 3.22
            }, {
                "produto": "arroz",
                "quantidade": 1,
                "valor": 10.34
            }, {
                "produto": "feijão",
                "quantidade": 2,
                "valor": 9.55
            }, {
                "produto": "batata",
                "quantidade": 10,
                "valor": 5.22
            }]
        }
        total = sum(p['quantidade'] * p['valor'] for p in produtos['produtos'])
        conteudo = json.dumps(produtos)
        self.mock_open.files['estoque.json'] = conteudo
        self.program()
        self.assertEqual(len(self.mock_open.opened),
                         0,
                         msg='Você se esqueceu de fechar o arquivo!')
        self.assert_printed(
            total,
            msg='Não funcionou para o arquivo que contém o seguinte texto: "{0}"'
            .format(conteudo))
