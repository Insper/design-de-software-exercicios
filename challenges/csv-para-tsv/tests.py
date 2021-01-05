from strtest import str_test


CSV = '''1,2,3
a,b,c
q,w,3
'''

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.mock_open.files['dados.csv'] = CSV
        self.program()
        self.assertEqual(len(self.mock_open.opened), 0)
        self.assertEqual(CSV.replace(',', '\t'), self.mock_open.files['dados.tsv'])
