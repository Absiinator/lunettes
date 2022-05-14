from django.test import TestCase
from numpy import product
from .models import *
from .forms import *
from costumer.models import *


# Create your tests here.
class CategoryTests(TestCase):

    def setUp(self):
        self.gender1 = Gender.objects.create(name='Male').save()
        self.gender2 = Gender.objects.create(name='Female').save()

    def Test_Category_create(self):
        self.categorytest = Category.objects.create(name="test").save()
        self.assertEqual(str(self.categorytest), 'test')


class ProductTests(CategoryTests):
   
    def setup_Products(self):
        categorytest_loaded = Category.objects.get(name='test')

        self.product1 = Product.objects.create(name="test", description="test", price=1.0, category=categorytest_loaded)
        self.product1.gender.set(self.gender1)
        
        self.product2 = Product.objects.create(name='test2', description='test object2', price=100, category=categorytest_loaded)
        self.product2.gender.set(self.gender2)

        self.product1.save()
        self.product2.save()

    def Test_Products_read(self):
        self.assertEqual(str(self.product2.description), 'test object2')

    def Test_Products_Modify(self):
        product = Product.objects.get(id=1)
        product.name = 'modifiedtest'
        product.save()

        self.assertEqual(str(product), 'modifiedtest')
