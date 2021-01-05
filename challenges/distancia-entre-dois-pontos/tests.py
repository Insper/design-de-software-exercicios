from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(10, 4, 10, 4), 0, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(10, 4, 11, 4), 1, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(10, 5, 10, 4), 1, places=3)

    def test_4(self):
        self.assertAlmostEquals(self.function(2, 3, 5, 7), 5, places=3)
