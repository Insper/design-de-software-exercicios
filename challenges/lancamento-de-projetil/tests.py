from strtest import str_test
import math

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.assertAlmostEquals(self.function(math.sqrt(9.8), math.pi / 6, 1), math.sqrt(3), places=3)
