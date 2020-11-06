from unittest import TestCase


def sum_num(num1, num2):
    return num1 + num2

class TestSum(TestCase):
    def test_sum_num(self):
        self.assertEqual(sum_num(10, 10), 20)
