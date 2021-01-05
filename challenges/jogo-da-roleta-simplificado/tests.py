'''
Faça um programa em Python que implementa o jogo da roleta simplificado, o usuário começa com 100 dinheiros, e o programa fica em loop até que o dinheiro acabe:

- O programa mostra a quantidade de dinheiro disponível (obrigatório o uso de `print`)
- O usuário aposta um valor (se o valor for zero o programa para)
- Posteriormente o programa pergunta se a aposta é em um número ou paridade (par/ímpar)
    - Se o usuário digitar a opção `'n'` o usuário digita o número de 1 a 36, caso ganhe ele recebe 35 vezes o que apostou
    - Se o usuário digitar a opção `'p'` o usuário escolhe se par (opção `'p'`) ou ímpar (opção `'i'`), caso ganhe ele recebe o mesmo que apostou
- Será feito um sorteio de 0 (zero) a 36 (trinta e seis) e na sequência o pagamento das apostas

Utilize a função `random.randint`.
'''

from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message(
        'Não funcionou quando o jogador pede para sair assim que o jogo começa.'
    )
    def test_sai_de_cara(self):
        self.mock_input.input_list = [0]
        self.mock_random.randint[(0, 36)] = [17]
        self.program()
        self.assert_printed_all([100])

    @str_test.error_message(
        'Não funcionou quando o jogador aposta tudo em paridade e perde.')
    def test_zera_de_cara_por_paridade(self):
        self.mock_input.input_list = [100, 'p', 'i']
        self.mock_random.randint[(0, 36)] = [12]
        self.program()
        self.assert_printed_all([100])

    @str_test.error_message(
        'Não funcionou quando o jogador aposta tudo em número e perde.')
    def test_zera_de_cara_por_numero(self):
        self.mock_input.input_list = [100, 'n', 11]
        self.mock_random.randint[(0, 36)] = [10]
        self.program()
        self.assert_printed_all([100])

    @str_test.error_message(
        "Não funcionou quando o jogador digita a seguinte entrada: 10, 'n', 11, 50, 'p', 'i', 40, 'n', 27, 100, 'n', 29, 3600, 'p', 'p'. Sendo que o jogador perde a primeira, ganha a segunda, perde a terceira, ganha a quarta e perde a quinta jogada."
    )
    def test_joga_e_perde(self):
        perde_numero_1 = [10, 'n', 11]
        ganha_paridade_2 = [50, 'p', 'i']
        perde_numero_3 = [40, 'n', 27]
        ganha_numero_4 = [100, 'n', 29]
        perde_paridade_5 = [3600, 'p', 'p']
        self.mock_input.input_list = perde_numero_1 + ganha_paridade_2 + perde_numero_3 + ganha_numero_4 + perde_paridade_5
        self.mock_random.randint[(0, 36)] = [10, 11, 25, 29, 1]
        self.program()
        self.assert_printed_all([100, 90, 140, 3600])

    @str_test.error_message(
        "Não funcionou quando o jogador digita a seguinte entrada: 10, 'n', 11, 50, 'p', 'i', 40, 'n', 27, 100, 'n', 29, 3600, 'p', 'p', 0. Sendo que o jogador perde a primeira, ganha a segunda, perde a terceira, ganha a quarta e ganha a quinta jogada."
    )
    def test_joga_e_sai(self):
        perde_numero_1 = [10, 'n', 11]
        ganha_paridade_2 = [50, 'p', 'i']
        perde_numero_3 = [40, 'n', 27]
        ganha_numero_4 = [100, 'n', 29]
        ganha_paridade_5 = [3600, 'p', 'p']
        sai = [0]
        self.mock_input.input_list = perde_numero_1 + ganha_paridade_2 + perde_numero_3 + ganha_numero_4 + ganha_paridade_5 + sai
        self.mock_random.randint[(0, 36)] = [10, 11, 25, 29, 2]
        self.program()
        self.assert_printed_all([100, 90, 140, 3600, 7200])
