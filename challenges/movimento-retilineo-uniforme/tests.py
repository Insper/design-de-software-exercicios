from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(0, 50, 100), 50, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(10, 0, 100), 1000, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(10, 500, 0), 500, places=3)

    def test_4(self):
        self.assertAlmostEquals(self.function(10, 50, 100), 1050, places=3)
