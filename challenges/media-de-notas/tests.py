from strtest import str_test


def gabarito_calcula_media(lista):
    count_alunos = 0
    notas_alunos = 0
    for l in lista:
        for d in l:
            notas_alunos += l[d]
            count_alunos += 1
    return notas_alunos / count_alunos


def calculo_errado(lista):
    count_turmas = 0
    medias = 0
    for l in lista:
        count_alunos = 0
        notas_alunos = 0
        for d in l:
            notas_alunos += l[d]
            count_alunos += 1
        medias += notas_alunos / count_alunos
        count_turmas += 1
    return medias / count_turmas


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        alunos = [{"aluno1": 5, "aluno2": 8}, {"aluno3": 5}]
        esperado = gabarito_calcula_media(alunos)
        errado = calculo_errado(alunos)
        obtido = self.function(alunos)
        msg = 'Exemplo do enunciado. Obtido: {0}. Esperado: {1}.'.format(
            obtido, esperado)
        try:
            self.assertAlmostEqual(errado, obtido)
            msg += ' O resultado é a média de todos os alunos, sem considerar as turmas.'
        except:
            pass
        self.assertAlmostEqual(esperado, obtido, msg=msg)

        turma1 = {
            "aluno1": 10.0,
            "aluno2": 8.0,
            "aluno3": 7.0,
            "aluno4": 9.5,
            "aluno5": 7.5,
        }
        turma2 = {
            "alunoa": 5.0,
            "alunob": 4.5,
            "alunoc": 6.5,
            "alunod": 8.5,
            "alunoe": 5.0,
        }
        turma3 = {
            "alunoA": 10.0,
            "alunoB": 9.5,
        }
        alunos = [turma1, turma2, turma3]

        esperado = gabarito_calcula_media(alunos)
        errado = calculo_errado(alunos)
        obtido = self.function(alunos)
        msg = 'Deveria funcionar para outros dicionários além dos mostrados no exemplo do enunciado. Obtido: {0}. Esperado: {1}.'.format(
            obtido, esperado)
        try:
            self.assertAlmostEqual(errado, obtido)
            msg += ' O resultado é a média de todos os alunos, sem considerar as turmas.'
        except:
            pass
        self.assertEqual(esperado, obtido, msg=msg)
