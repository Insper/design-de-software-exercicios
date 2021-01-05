from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        words = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua tincidunt dui ut ornare lectus sit amet est placerat eget nunc lobortis mattis aliquam faucibus purus in massa est ultricies integer quis auctor elit sed egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla et ligula ullamcorper malesuada proin libero dignissim convallis aenean et tortor at risus nunc sed augue lacus viverra sed sed risus pretium quam vulputate dignissim suspendisse lectus arcu bibendum at varius vel quis imperdiet massa tincidunt nunc pulvinar sapien et sit amet cursus sit amet dictum sit amet justo donec iaculis nunc sed augue lacus viverra id venenatis a condimentum vitae sapien pellentesque habitant morbi tristique enim blandit volutpat maecenas volutpat neque vitae tempus quam pellentesque nec nam aliquam sit amet nisl suscipit adipiscing bibendum tincidunt vitae semper quis lectus nulla at ullamcorper eget nulla facilisi etiam dignissim fim'.split()
        words_to_print = [w for w in words if w[0] == 'a']
        self.mock_input.input_list = words + 'mais umas palavras'.split()
        self.program()
        self.assertEqual(self.mock_input.calls, len(words), 'Não terminou no momento certo.')
        self.assertEqual(self.mock_print.calls, len(words_to_print), 'Imprimiu uma quantidade de palavras diferente do esperado.')
        self.assertEqual(self.mock_print.printed, words_to_print)

    def test_stop(self):
        self.mock_input.input_list = ['fim'] + 'mais umas palavras'.split()
        self.program()
        self.assertEqual(self.mock_input.calls, 1, 'Não funcionou quando a primeira palavra é "fim".')
