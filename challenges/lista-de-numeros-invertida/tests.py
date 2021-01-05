from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        nums = [1,4,2,6,3,0]
        self.mock_input.input_list = nums
        self.program()
        self.assertEqual(self.mock_input.calls, len(nums))
        i = len(nums) - 2
        for printed in self.mock_print.printed:
            self.assertTrue(str(nums[i]) in printed, 'Não funcionou para o elemento {0} de {1}. O programa imprimiu "{2}"'.format(nums[i], nums, printed))
            i -= 1
            if i < 0:
                break

    def test_2(self):
        nums = [6,3,7,8,3,4,7,5,345,7,865,-10]
        self.mock_input.input_list = nums
        self.program()
        self.assertEqual(self.mock_input.calls, len(nums))
        i = len(nums) - 2
        for printed in self.mock_print.printed:
            self.assertTrue(str(nums[i]) in printed, 'Não funcionou para o elemento {0} de {1}. O programa imprimiu "{2}"'.format(nums[i], nums, printed))
            i -= 1
            if i < 0:
                break

    def test_3(self):
        nums = [0]
        self.mock_input.input_list = nums
        self.program()
        self.assertEqual(self.mock_input.calls, len(nums))

    def test_4(self):
        nums = [-134]
        self.mock_input.input_list = nums
        self.program()
        self.assertEqual(self.mock_input.calls, len(nums))
