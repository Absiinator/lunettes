from django.test import TestCase
from numpy import product
from .models import *
from .forms import *
from costumer.models import *


# Create your tests here.
class CRUDTest(TestCase):

    # first test is needed to setup the database
    def test_CRUD(self):
        # need to initialize genders in the database to create objects
        gender1 = Gender.objects.create(name='Male')
        gender2 = Gender.objects.create(name='Female')

        gender1.save()
        gender2.save()

        gender1_loaded = Gender.objects.filter(name='Male')
        gender2_loaded = Gender.objects.filter(name='Female')

        categorytest = Category.objects.create(name="test")
        categorytest.save()

        categorytest_loaded = Category.objects.get(name='test')

        self.assertEqual(str(categorytest_loaded), 'test')

        product1 = Product.objects.create(name="test", description="test", price=1.0, category=categorytest_loaded)
        product1.gender.set(gender1_loaded)
        product2 = Product.objects.create(name='test2', description='test object2', price=100, category=categorytest_loaded)
        product2.gender.set(gender2_loaded)

        product1.save()
        product2.save()

        self.assertEqual(str(product1), 'test')

        # modify values on products
        product1 = Product.objects.get(id=1)
        product1.name = 'modifiedtest'
        product1.save()

        self.assertEqual(str(product1), 'modifiedtest')
        self.assertEqual(str(product2.description), 'test object2')
        self.assertEqual(str(categorytest), 'test')
