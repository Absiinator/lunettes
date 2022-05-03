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
    def test_setUp(self):
        # need to add path to join pictures on models
        BASE_DIR = Path(__file__).resolve().parent.parent

        # genders are mentatory to create before anything else/
        gender1 = Gender.objects.create(name='Male')
        gender2 = Gender.objects.create(name='Female')

        gender1.save()
        gender2.save()
        
        # import and read cv
        datapath = os.path.join(BASE_DIR, 'lunettes/static/userdatabase/users.csv')
        df = pd.read_csv(datapath)
        for index, row in df.iterrows():
            gender = Gender.objects.get(name=row['gender'])

            costumer = Costumer.objects.create(
                username =  row['username'],
                gender =    gender,
            )
                    
        Dummy_database.objects.create(loaded=True)
        costumer = Costumer.objects.get(id=12)

        self.assertEqual(str(costumer), 'Beatrice')

    