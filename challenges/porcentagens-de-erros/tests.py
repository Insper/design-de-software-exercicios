from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        args = [
            {'Erro de indentação': 493, 'Erro de parênteses': 1102, 'Variável inexistente': 405},
            {'Erro de indentação': 5, 'Erro de parênteses': 5, 'Variável inexistente': 10},
            {'Erro tipo 1': 1000, 'Erro tipo 2': 3000, 'Erro tipo 3': 6000},
            {'Erro único': 1},
        ]
        for dicionario in args:
            obtido = self.function(dicionario)
            total = sum(dicionario.values())
            esperado = {erro: absoluto * 100 / total for erro, absoluto in dicionario.items()}
            for chave in dicionario:
                self.assertIn(chave, obtido, msg=f"A chave '{chave}' não existe no dicionário devolvido pela sua função.")
                msg = f"Não funcionou para entrada={dicionario}. O valor obtido para a chave '{chave}' foi {obtido[chave]}. O valor esperado era {esperado[chave]}."
                self.assertAlmostEqual(obtido[chave], esperado[chave], msg=msg)
