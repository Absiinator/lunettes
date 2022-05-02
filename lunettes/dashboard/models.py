from django.db import models

# Create your models here.
class Dummy_database(models.Model):
    loaded = models.BooleanField(default=False)

    def __str__(self):
        return str('Dummy database is loaded : '+self.loaded)