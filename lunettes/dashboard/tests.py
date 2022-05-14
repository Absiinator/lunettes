from django.test import TestCase
from .models import *
import os
from pathlib import Path
from django.core.files.images import ImageFile
import tempfile
import pandas as pd
import pickle

from costumer.models import *
from costumer.getPredictions import *
from products.models import *

# Create your tests here.
class DashboardTestCase(TestCase):

    def setUp(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.datapath = os.path.join(self.BASE_DIR, 'lunettes/static/userdatabase/users.csv')
        self.df = pd.read_csv(self.datapath)
        self.gender1 = Gender.objects.create(name='Male').save()
        self.gender2 = Gender.objects.create(name='Female').save()


    def test_Imports(self):
        
        for index, row in self.df.iterrows():
            gender = Gender.objects.get(name=row['gender'])

            costumer = Costumer.objects.create(
                username =  row['username'],
                gender =    gender,
            )
                    
        costumer = Costumer.objects.get(id=12)

        self.assertEqual(str(costumer), 'Beatrice')