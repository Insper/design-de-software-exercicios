from strtest import str_test
import math

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(4, 5), 3, places=3)

    def test_2(self):
        self.assertAlmostEquals(self.function(3, 5), 4, places=3)

    def test_3(self):
        self.assertAlmostEquals(self.function(1, math.sqrt(2)), 1, places=3)

