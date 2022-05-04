# Lunettes - Optic 3000
## Projet chef d'oeuvre Simplon

Please install requirements.txt with following commands :  
> pip install -r requirements.txt

Make sure you created an virtual environnement before installing dependencies.  
Model was trained and project was run on M1 equiped Macbook Pro. Please check your tensorflow installation.  

## Before running the server
You can execute the tests to see if everything will work fine in the backend.  
> cd lunettes
> python3 manage.py makemigrations  
> python3 manage.py migrate  
> python3 manage.py test  

If no error is detected, you can procede.
## When running the server for the first time

authentification can be achieved by creating a superuser
> cd lunettes  
> python3 manage.py createsuperuser

By default I recommand creating a simlpe admin/admin  
Django will automatically create genders when logging into the dashboard. This happens if the number of genre is not 2 !   
You cannot make more than 2 genders !  
This model is not capable of scalling.  

### Init with dummy database
You can then import the dummy database by pressing the button on the dashboard.  
This can only happen ONCE, due to the risk of flooding the database with copies.  
The dummy dataset is then fully processed by the prediction.  
You only have to create a product category and create products of your liking. 