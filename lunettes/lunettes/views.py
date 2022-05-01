from hashlib import new
from re import I, S
import weakref
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import Unauthenticated_user
from django.template import RequestContext


def Authentification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Nom d'Utilisateur ou Mot De Passe incorrect")

    return render(request, "authentification.html")

@login_required(login_url='authentification')
def LogoutUser(request):
    logout(request)
    return redirect('authentification')