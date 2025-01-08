from django.test import TestCase
from .utils import multiply
from django.urls import reverse
from .models import Item

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

class ItemCrudTest(TestCase):

    def test_create_item(self):
        """Mengujikan pembuatan item baru."""
        response = self.client.post(reverse('create_item'), {'name': 'Test Item', 'price': 10000})
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
       

