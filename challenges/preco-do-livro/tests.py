from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        livros = {
            "Pinóquio": "azul",
            "Dom Quixote": "amarelo",
            "O Pequeno Príncipe": "vermelho",
        }
        cores = {
            "vermelho": 10.0,
            "azul": 20.0,
            "amarelo": 40.0,
            "verde": 100.0,
        }
        for titulo in livros:
            esperado = cores[livros[titulo]]
            obtido = self.function(titulo, livros, cores)
            msg = 'Exemplo do enunciado. Título: {2}. Obtido: {0}. Esperado: {1}'.format(
                obtido, esperado, titulo)
            self.assertEqual(esperado, obtido, msg=msg)

        livros = {
            "Musashi": "rosa",
            "Harry Potter e a Pedra Filosofal": "cinza",
            "O Hobbit": "branco",
            "O Senhor dos Anéis": "roxo",
            "O Leão, a Feiticeira e o Guarda-Roupa": "marrom",
            "O Código Da Vinci": "cinza",
            "O Apanhador no Campo de Centeio": "rosa",
        }
        cores = {
            "rosa": 15.0,
            "cinza": 25.0,
            "branco": 35.0,
            "roxo": 200.0,
            "marrom": 1000.0,
        }
        for titulo in livros:
            esperado = cores[livros[titulo]]
            obtido = self.function(titulo, livros, cores)
            msg = 'Deveria funcionar para outros dicionários além dos mostrados no exemplo do enunciado. Título: {2}. Obtido: {0}. Esperado: {1}'.format(
                obtido, esperado, titulo)
            self.assertEqual(esperado, obtido, msg=msg)
