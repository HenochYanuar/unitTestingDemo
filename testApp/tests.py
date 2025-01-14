from django.test import TestCase
from .utils import multiply
from django.urls import reverse
from .models import Item
from submoduleUnitTesting.function import devided_function, minus_function
from .validators import ProductValidator
from pydantic import ValidationError

# Create your tests here.

class testMultiplyFunction(TestCase):

  def test_positive_numbers_input(self):
    """Menguji perkalian dua angak positif"""
    self.assertEqual(multiply(2, 5), 10)

  def test_negative_numbers_input(self):
    """Menguji perkalian dua angka negatif"""
    self.assertEqual(multiply(-2, -5), 10)

  def test_negative_and_positive_input(self):
    """Menguji perkalian angka negatif dan positif"""
    self.assertEqual(multiply(-2, 5), -10)

  def test_multiply_by_zero_input(self):
    """Menguji perkalian dengan angka 0"""
    self.assertEqual(multiply(2, 0), 0)
    self.assertEqual(multiply(0, 2), 0)

class testDevidedFunction(TestCase):
   
  def test_positive_numbers_input(self):
    """Menguji pembagian dengan input positif"""
    self.assertEqual(devided_function(10, 2), 5)

  def test_negatif_numbers_input(self):
     """Menguji pembagian dengan input negatif"""
     self.assertEqual(devided_function(-10, -2), 5)

  def test_negative_and_positive_numbers_input(self):
     """Menguji pembagian dengan input negative and positive"""
     self.assertEqual(devided_function(-10, 2), -5)

  def test_devided_with_fraction_return(self): 
     """Menguji pembagian dnegan hasil pecahan"""
     self.assertEqual(devided_function(2, 5), 0.4)

class testMinusFUnction(TestCase):
   
  def test_positive_number_inputs(self):
    """Menguji pengurangan dengan input positif"""
    self.assertEqual(minus_function(10, 2), 8)

  def test_negative_number_inputs(self):
     """Menguji pengurangan dengan input negatif"""
     self.assertEqual(minus_function(-10, -2), -8)

  def test_return_negative(self):
     """Menguji pengurangan dengan hasil negatif"""
     self.assertEqual(minus_function(10, 20), -10)

class ItemCrudTest(TestCase):

    def test_create_item(self):
        """Mengujikan pembuatan item baru."""
        data = {
           'name': 'Test Item', 
           'price': 10000,
           'email': 'contoh@contoh.com',
           'code': 'abcd1234'

        }
        product = ProductValidator(**data)
        response = self.client.post(reverse('create_item'), product.dict())
        self.assertEqual(product.name, 'Test Item')
        self.assertEqual(product.price, 10000)
        self.assertEqual(response.status_code, 201)

    def test_get_item(self):
        """Mengujikan pengambilan item berdasarkan ID."""
        item = Item.objects.create(name='Test Item', price=10000)
        response = self.client.get(reverse('get_item', args=[item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'name': item.name, 'price': f"{item.price:.2f}"})

    def test_update_item(self):
       """Mengujikan update item berdasarkan ID."""
       item = Item.objects.create(name='Test Item', price=10000)
       response = self.client.post(reverse('update_item', args=[item.id]), {'name': 'Update Test Item', 'price': 20000})
       self.assertEqual(response.status_code, 200)
       self.assertEqual(Item.objects.get(id=item.id).name, 'Update Test Item')
       self.assertEqual(Item.objects.get(id=item.id).price, 20000)

    def test_delete_item(self):
       """Mengujikan penghapusan item berdasarkan ID."""
       item = Item.objects.create(name='Test Item', price=10000)
       response = self.client.delete(reverse('delete_item', args=[item.id]))
       self.assertEqual(response.status_code, 204)
       

