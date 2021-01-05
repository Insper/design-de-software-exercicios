from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        lists = [[0], [1,2,3], [-5,10,2,7,-6543,314,2,-543,123536], [-1,-2,-3,4]]
        expected = [[0], [1,2,3], [0,10,2,7,0,314,2,0,123536], [0,0,0, 4]]
        for l, e in zip(lists, expected):
            self.assertEqual(self.function(l), e, 'Não funcionou para a lista {0}'.format(l))
