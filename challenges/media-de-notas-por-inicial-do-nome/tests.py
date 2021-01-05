from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    # Possível solução
    def medias_por_inicial(entrada):
        letras = {}
        for nome in entrada:
            if nome[0] in letras:
                letras[nome[0]].append(entrada[nome])
            else:
                letras[nome[0]] = [entrada[nome]]
        
        for letra in letras:
            tamanho = len(letras[letra])
            soma = 0
            for letra_soma in letras[letra]:
                soma += letra_soma
            letras[letra] = soma/tamanho

        return letras

    def test_1(self):
        entradas = [{'Andrew Ayres': 6, 'FÃ¡bio Ikeda': 10, 'FÃ¡bio Kurauchi': 9, 'Raul Hage': 8}]
        esperados = [{'A': 6, 'F': 9.5, 'R': 8}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'NÃ£o funcionou para a entrada {0}'.format(entrada))

    def test_2(self):
        entradas = [{'Andrew Ayres': 6, 'FÃ¡bio Ikeda': 10, 'FÃ¡bio Kurauchi': 9, 'Raul Hage': 8, 'Fabio Beltrano': 6, 'Fernando Fulano': 9, }]
        esperados = [{'A': 6.0, 'F': 8.5, 'R': 8.0}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'NÃ£o funcionou para a entrada {0}'.format(entrada))