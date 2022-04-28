from calendar import c
from re import I
from django.shortcuts import render
from .decorators import *
from django.contrib.auth.decorators import login_required
import pandas as pd

from costumer.models import *
from products.models import *

# Create your views here.
@login_required(login_url='authentification')
def dashboard(request):
    products = Product.objects.all()
    costumers = Costumer.objects.all()

    # create a dataframe of gender distribution
    dist_df = pd.DataFrame({'Male': [costumers.filter(gender__name='Male').count()], 
                        'Female': [costumers.filter(gender__name='Female').count()]})


    context = {'pageActive': 'Dashboard',
                'products': products,
                'distribution': dist_df}
    return render(request, 'dashboard/dashboard.html', context)