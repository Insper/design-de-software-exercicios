from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        all_args = [
            (["André", "Carlos", "João", "Otavio", "Thiago"], [2, 3]),
            (["BRENO", "CARLOS", "ERIC", "EDUARDO", "ALICE", "Sarah", "STEPHAN", "LORENA", "LETÍCIA", "ADNEY", "JERÔNIMO", "NÍVEA", "GABRIEL", "RODRIGO", "LUCCA", "YKARO", "CARLOS", "Gabriel", "RODRIGO", "EDUARDO", "PAULO", "RENATO", "ANDRÉ", "LUCAS", "LUÍSA", "JOAO", "RICARDO", "KEIYA", "LISTER", "GABRIEL", "PEDRO", "FELIPE", "MATHEUS", "FLAVIO", "CELINA", "GABRIEL"], [6, 30]),
        ]
        for lista, esperado in all_args:
            obtido = self.function(lista)
            self.assertEqual(obtido, esperado, msg=f'Não funcionou para a lista {lista}. Valor esperado: {esperado}. Valor obtido: {obtido}')
