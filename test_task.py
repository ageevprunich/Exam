import unittest
from task import ArithmeticProgression

class TestArithmeticProgression(unittest.TestCase):
    def test_calculate_sum(self):
        progression = ArithmeticProgression(first=4, difference=3)

        result = progression.calculate_sum(1)
        self.assertEqual(result, 4)

        result = progression.calculate_sum(2)
        self.assertEqual(result, 11)

        result = progression.calculate_sum(3)
        self.assertEqual(result, 21)

    def wrong_answer(self):
        progression = ArithmeticProgression(first=4, difference=3)
        result = progression.calculate_sum(4)
        self.assertNotEqual(result, 30)
    
    def type_check(self):
        progression = ArithmeticProgression(first=4, difference=3)
        with self.assertRaises(TypeError):
            progression.calculate_sum("invalid_input")


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()