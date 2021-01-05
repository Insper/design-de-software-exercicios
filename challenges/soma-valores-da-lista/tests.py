from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        lists = [[0], [1,2,3], [-5,10,2,7,-6543,314,2,-543,123536]]
        for l in lists:
            self.assertEqual(self.function(l), sum(l), 'Não funcionou para a lista {0}'.format(l))
