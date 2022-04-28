from unicodedata import category
from django.db import models
from costumer.models import Gender

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='products/images', blank=True, null=True)
    gender = models.ManyToManyField(Gender)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name
