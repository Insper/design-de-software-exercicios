"""
Read strtest docs for more details: https://github.com/Insper/python-string-test-runner

Quick Guide:
===========
TestCaseWrapper has the following attributes:
    - function: function given by the user
    - program: function that executes the program given by the user
    - module: python module loaded from the file given by the user
Useful asserts:
    - assert_similar(self, string1, string2, dist_max=1, case_sensitive=False, msg=None)
    - assert_printed(self, value, index=None, msg=None)
    - assert_printed_all(self, values, msg=None, **kwargs)
Mocks (all functions have the attributes calls, args, and kwargs, that store the call count and arguments):
    - mock_print: printed attribute stores a list of printed strings
    - mock_input: set input_list with a sequence of inputs to be used
    - mock_open: the attribute opened is a list of files that have not been closed and it is possible to add mock files in the dictionary attribute 'files' (keys are the filenames and values are their content)
    - mock_random: keys are tuples with the expected arguments and the values are sequences of numbers

If you implement the methods setUpClass, setUp, or tearDown, remember to call the superclass implementation.
"""
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    @str_test.error_message('Verificar quando distância percorrida é zero')
    def test_distancia_zero(self):
        self.assertAlmostEquals(self.function(0, 1), 0.0)

    @str_test.error_message('Verificar quando o valor da distância e do tempo são iguais')
    def test_distancia_tempo_iguais(self):
        self.assertAlmostEquals(self.function(1, 1), 1.0)

    @str_test.error_message('Verificar quando o tempo não é inteiro')
    def test_tempo_float(self):
        self.assertAlmostEquals(self.function(1, 0.1), 10.0)

    @str_test.error_message('Verificar quando a distância não é inteira')
    def test_distancia_float(self):
        self.assertAlmostEquals(self.function(0.1, 1), 0.1)

    @str_test.error_message('Verificar quando a velocidade média não é inteira')
    def test_velocidade_media_float(self):
        self.assertAlmostEquals(self.function(1, 2), 0.5)

    @str_test.error_message('Verificar quando distância percorrida é grande (> 1000 km)')
    def test_distancia_grande(self):
        self.assertAlmostEquals(self.function(1098, 9), 122)
