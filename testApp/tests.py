from django.test import TestCase
from .utils import multiply

# Create your tests here.

class testMultiplyFunction(TestCase):

  def test_positive_numbers_input(self):
    # Menguji perkalian dua angak positif
    self.assertEqual(multiply(2, 5), 10)

  def test_negative_numbers_input(self):
    # Menguji perkalian dua angka negatif
    self.assertEqual(multiply(-2, -5), 10)

  def test_negative_and_positive_input(self):
    # Menguji perkalian angka negatif dan positif
    self.assertEqual(multiply(-2, 5), -10)

  def test_multiply_by_zero_input(self):
    # Menguji perkalian dengan angka 0
    self.assertEqual(multiply(2, 0), 0)
    self.assertEqual(multiply(0, 2), 0)