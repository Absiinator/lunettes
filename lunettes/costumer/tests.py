from django.test import TestCase
from .models import *
from .forms import *
from .getPredictions import *

import os
from pathlib import Path


class CRUDTest(TestCase):
    def test_CRUD(self):
        # need to add path to join pictures on models
        BASE_DIR = Path(__file__).resolve().parent.parent

        # genders are mentatory to create before anything else/
        gender1 = Gender.objects.create(name='Male')
        gender2 = Gender.objects.create(name='Female')

        gender1.save()
        gender2.save()

        gender1_loaded = Gender.objects.get(name='Male')
        gender2_loaded = Gender.objects.get(name='Female')

        # loading images paths
        image1 = os.path.join(BASE_DIR, 'media/tests/images/testBoy.jpeg')
        image2 = os.path.join(BASE_DIR, 'media/tests/images/testGirl.jpeg')

        # Creating costumers
        costumer_test1 = Costumer.objects.create(username='testBoy', gender=gender1_loaded, image=image1)
        costumer_test2 = Costumer.objects.create(username='testGirl', gender=gender2_loaded, image=image2)

        costumer_test1.save()
        costumer_test2.save()

        self.assertEqual(str(costumer_test1), 'testBoy')
        self.assertEqual(str(costumer_test2), 'testGirl')
    
    def test_Preditions(self):
        
        # Initializing test image path and model path
        # this is done to solely test the predictions, views use a function to return path from uploaded images in databases
        BASE_DIR = Path(__file__).resolve().parent.parent
        image1 = os.path.join(BASE_DIR, 'media/tests/images/testBoy.jpeg')
        image2 = os.path.join(BASE_DIR, 'media/tests/images/testGirl.jpeg')
        model = pickle.load(open(f'{BASE_DIR}/lunettes/static/AI/model.pkl', 'rb'))

        # getting predictions
        result = get_prediction(image1, model=model)[1]
        result2 = get_prediction(image2, model=model)[1]

        self.assertEqual(result, 'Male')
        self.assertEqual(result2, 'Female')       
