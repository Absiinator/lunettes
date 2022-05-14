from django.test import TestCase
from .models import *
from .forms import *
from .getPredictions import *

import os
from pathlib import Path


class CRUDTest(TestCase):

    def setUp(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.datapath = os.path.join(self.BASE_DIR, 'lunettes/static/userdatabase/users.csv')
        self.gender1 = Gender.objects.create(name='Male').save()
        self.gender2 = Gender.objects.create(name='Female').save()
        self.image1 = os.path.join(self.BASE_DIR, 'media/tests/images/testBoy.jpeg')
        self.image2 = os.path.join(self.BASE_DIR, 'media/tests/images/testGirl.jpeg')
        self.model = pickle.load(open(f'{self.BASE_DIR}/lunettes/static/AI/model.pkl', 'rb'))


    def test_CRUD(self):

        gender1_loaded = Gender.objects.get(name='Male')
        gender2_loaded = Gender.objects.get(name='Female')

        costumer_test1 = Costumer.objects.create(username='testBoy', gender=gender1_loaded, image=self.image1)
        costumer_test2 = Costumer.objects.create(username='testGirl', gender=gender2_loaded, image=self.image2)

        costumer_test1.save()
        costumer_test2.save()

        self.assertEqual(str(costumer_test1), 'testBoy')
        self.assertEqual(str(costumer_test2), 'testGirl')
    
    def test_Preditions(self):
        # getting predictions
        result = get_prediction(self.image1, model=self.model)[1]
        result2 = get_prediction(self.image2, model=self.model)[1]

        self.assertEqual(result, 'Male')
        self.assertEqual(result2, 'Female')       
