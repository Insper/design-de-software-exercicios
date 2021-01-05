from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        all_args = [
            (("ada", "inha", "ada", "inha"), "alternada"),
            (("ados", "mento", "mento", "ados"), "interpolada"),
            (("ada", "ada", "rocha", "rocha"), "emparelhada"),
            (("ados", "mento", "mento", "inha "), "outra"),
            (("ada", "ada", "ada", "ada"), "outra"),
        ]
        for args, esperado in all_args:
            obtido = self.function(*args)
            self.assertEqual(obtido, esperado, msg=f'Não funcionou para as sílabas "{args[0]}", "{args[1]}", "{args[2]}" e "{args[3]}".')
