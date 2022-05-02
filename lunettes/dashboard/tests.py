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

        gender1_loaded = Gender.objects.get(name='Male')
        gender2_loaded = Gender.objects.get(name='Female')

        model = pickle.load(open(f'{BASE_DIR}/lunettes/static/AI/model.pkl', 'rb'))

        # import and read cv
        # note that csv file must contain a path to a image file for each costumer
        datapath = os.path.join(BASE_DIR, 'lunettes/static/userdatabase/users.csv')
        df = pd.read_csv(datapath)
        for index, row in df.iterrows():
            image_path = os.path.join(BASE_DIR, 'lunettes/static/userdatabase/'+str(row['image_path']))
            gender = Gender.objects.get(name=row['gender'])

            # Django handles poorly imports files when not in forms. This method is required to input files through model.objects.create() django method
            dummy_file_name = str(row['image_path']).split('/')[-1]

            lf = tempfile.NamedTemporaryFile(dir='media')   # create a temporary file
            f = open(image_path, 'rb')                      # open the image file
            lf.write(f.read())                              # write the image file to the temporary file

            # Then procede with normal django imports methods

            costumer = Costumer.objects.create(
                username =  row['username'],
                gender =    gender,
            )
            
            costumer = Costumer.objects.get(id=costumer.id)
            costumer.image.save(dummy_file_name, ImageFile(lf)) # this syntax is required

            image = get_file_path(costumer_image=costumer.image.url)
            predictions = get_prediction(image, model=model)[1]
            costumer.prediction = predictions
            costumer.save()
        
        Dummy_database.objects.create(loaded=True)