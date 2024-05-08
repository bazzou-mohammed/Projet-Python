from unittest import TestCase
from calc import multiply

class TestCalculatrice(TestCase):
    def test_mul_two_numbers(self):
        self.assertEqual(multiply(-5, 0), 0)
