from unittest import TestCase
from somar import adicao

class TestSum(TestCase):
    def test_adicao(self):
        self.assertEqual(adicao(10, 10), 20)
