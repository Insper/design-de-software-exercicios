from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(0, 10), 0, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(10, 0), 0, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(1, 1), 3.141592, places=3)

    def test_4(self):
        self.assertAlmostEquals(self.function(10, 2), 628.3185, places=3)

