from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def costumersList(request):
    costumers = Costumer.objects.all()
    context = {
        'pageActive': 'Costumers',
        'costumers': costumers,
    }
    return render(request, 'costumers/costumers.html', context)

def costumersDetails(request, id):
    costumer = Costumer.objects.get(id=id)
    context = {
        'pageActive': 'Costumers',
        'costumer': costumer,
    }
    return render(request, 'costumers/costumersDetails.html', context)

def costumersCreate(request):
    form = CostumerForm()
    if request.method == 'POST':
        form = CostumerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(costumersList)

    context = {
        'pageActive': 'Costumers',
        'CostumerForm': form,
    }
    return render(request, 'costumers/costumersCreate.html', context)

def costumersModify(request, id):
    costumer = Costumer.objects.get(id=id)
    form = CostumerForm(instance=costumer)
    if request.method == 'POST':
        form = CostumerForm(request.POST, request.FILES, instance=costumer)
        if form.is_valid():
            form.save()
            return redirect(costumersDetails, id)

    context = {
        'pageActive': 'Costumers',
        'costumer': costumer,
        'CostumerForm': form,
    }
    return render(request, 'costumers/costumersModify.html', context)

def costumersDelete(request, id):
    costumer = Costumer.objects.get(id=id)
    costumer.delete()
    return redirect(costumersList)