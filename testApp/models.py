from django.db import models
from faker import Faker

# Create your models here.

fake = Faker()

class Item(models.Model):
    # id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=8, null=True)


    def __str__(self):
        return self.name

# membuat faker untuk class Item
def create_faker_item():
    item = Item()
    # item.id = fake.random_int(min=1111, max=9999)
    item.name = fake.name()
    item.price = fake.random_int(min=1000, max=99999)
    item.email = fake.email()
    item.code = fake.random_int(min=10000000, max=99999999)
