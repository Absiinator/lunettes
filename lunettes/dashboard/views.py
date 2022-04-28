from django.shortcuts import render
from .decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='authentification')
def dashboard(request):
    context = {'pageActive': 'dashboard'}
    return render(request, 'dashboard/dashboard.html', context)