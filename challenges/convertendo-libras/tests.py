from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(0), 0.0, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(1), 0.453592, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(2.20462), 1, places=3)

    def test_4(self):
        self.assertAlmostEquals(self.function(100), 45.3592, places=3)
