from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(0), 0, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(10), 4188.79, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(1), 4.18879, places=3)
