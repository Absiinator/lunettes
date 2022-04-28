from django.db import models


class Gender(models.Model):
    Gender = models.TextField(max_length=10, blank=False, null=False),


class Costumer(models.Model):

    username = models.CharField(max_length=255)
    gender = models.OneToOneField(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return self.name