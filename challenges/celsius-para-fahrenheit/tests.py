from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(0), 32, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(100), 212, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(37.7778), 100, places=3)
