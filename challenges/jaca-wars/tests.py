import math
from strtest import str_test


def calcula_distancia(velocidade, angulo_graus):
    angulo = math.radians(angulo_graus)
    g = 9.8
    return velocidade**2 * math.sin(2 * angulo) / g


def gabarito_dos_professores(distancia):
    if distancia - 100 < -2:
        return 'Muito perto'
    elif distancia - 100 > 2:
        return 'Muito longe'
    else:
        return 'Acertou!'


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        velocidades = list(range(30, 40))
        velocidades.append(33.97408804020941)  # Pois é...
        for velocidade in velocidades:
            for angulo in range(20, 40):
                distancia = calcula_distancia(velocidade, angulo)
                resposta = gabarito_dos_professores(distancia)
                if distancia != 98 and distancia != 102:
                    self.mock_input.input_list.append(velocidade)
                    self.mock_input.input_list.append(angulo)
                    self.program()
                    self.assertTrue(resposta in self.mock_print.printed[-1])
