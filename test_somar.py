from unittest import TestCase
import somar as s


class TestSum(TestCase):
    def test_adicao(self):
        self.assertEqual(s.adicao(10, 10), 20)

    def test_subtracao(self):
        self.assertEqual(s.subtracao(50, 10), 40)

    def test_delta(self):
        self.assertEqual(s.delta(2, 5, 8), -54)

    def test_check_delta(self):
        self.assertTrue(s.check_delta(10), True)
        self.assertFalse(s.check_delta(-10), False)

    def test_calc_raizes(self):
        self.assertEqual(s.calc_raizes(10, 10, 10), None)

    def test_baskara(self):
        self.assertEqual(s.baskara(4, 80, 2), None)
        self.assertEqual(s.baskara(2, 5, 8), False)

    def test_check_name(self):
        self.assertEqual(s.check_name('10'), 10)
        with self.assertRaises(Exception):
            self.assertEqual(s.check_name('silva'), Exception)
