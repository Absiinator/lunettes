from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=32, default='Male')

    def __str__(self):
        return self.name




class Costumer(models.Model):

    username = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='costumers/images', blank=True, null=True, max_length=255)
    prediction = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username