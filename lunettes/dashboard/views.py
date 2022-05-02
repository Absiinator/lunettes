from django.shortcuts import render
from .decorators import *
from django.contrib.auth.decorators import login_required
import pandas as pd
import os
from pathlib import Path
from django.core.files.images import ImageFile
import shutil
from PIL import Image
import tempfile

from costumer.getPredictions import *
from costumer.models import *
from costumer.views import *
from products.models import *
from .models import *

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
@login_required(login_url='authentification')
def dashboard(request):
    # if genders len != 2 or >2 then create (or delete all then create) genders in database.
    genders = Gender.objects.all()
    if len(genders)!=2:
        Gender.objects.all().delete()
        Gender.objects.create(name='Male')
        Gender.objects.create(name='Female')
    
    products = Product.objects.all()[:10]
    costumers = Costumer.objects.all()
    dataloaded = Dummy_database.objects.all().count()
    

    # create a dataframe of gender distribution
    dist_df = pd.DataFrame({'Male': [costumers.filter(gender__name='Male').count()], 
                        'Female': [costumers.filter(gender__name='Female').count()]})


    context = {'pageActive': 'Dashboard',
                'products': products,
                'distribution': dist_df,
                'dataloaded': dataloaded}
    return render(request, 'dashboard/dashboard.html', context)

# import dummies from csv
def Import_database(request):
    if Dummy_database.objects.all().count() == 0: # if database is not loaded
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
        
        Dummy_database.objects.create(loaded=True) # set loaded to true to avoid multiple imports
        return redirect(costumersList)
    else:
        return redirect(costumersList)