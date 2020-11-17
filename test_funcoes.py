from unittest import TestCase
import funcoes

class Testes(TestCase):

    def test_adicao(self):
        self.assertEqual(funcoes.adicao(20, -10), 10)

    def test_subtracao(self):
        self.assertEqual(funcoes.subtracao(50, 10), 40)

    def test_delta(self):
        self.assertEqual(funcoes.delta(2, 5, 8), -54)

    def test_check_delta(self):
        self.assertTrue(funcoes.check_delta(10), True)
        self.assertFalse(funcoes.check_delta(-10), False)

    def test_calc_raizes(self):
        self.assertEqual(funcoes.calc_raizes(10, 10, 10), None)

    def test_baskara(self):
        self.assertEqual(funcoes.baskara(4, 80, 2), None)
        self.assertEqual(funcoes.baskara(2, 5, 8), False)

    def test_check_name(self):
       self.assertEqual(funcoes.check_name('10'), 10)
       with self.assertRaises(Exception):
           self.assertEqual(funcoes.check_name('silva'), Exception)