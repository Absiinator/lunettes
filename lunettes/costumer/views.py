from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .getPredictions import *
from .decorators import *
from django.contrib.auth.decorators import login_required


from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import pickle

# loading model on server start
BASE_DIR = Path(__file__).resolve().parent.parent
model = pickle.load(open(f'{BASE_DIR}/lunettes/static/AI/model.pkl', 'rb'))

# Create your views here.
@login_required(login_url='authentification')
def costumersList(request):
    costumers = Costumer.objects.all()[::-1]
    context = {
        'pageActive': 'Costumers',
        'costumers': costumers,
    }
    return render(request, 'costumers/costumers.html', context)

@login_required(login_url='authentification')
def costumersDetails(request, id):
    costumer = Costumer.objects.get(id=id)
    declared_gender = str(costumer.gender)

    context = {
        'pageActive': 'Costumers',
        'costumer': costumer,
        'declared_genre': declared_gender # this is needed in order to compare string to string values in template
    }
    return render(request, 'costumers/costumersDetails.html', context)

@login_required(login_url='authentification')
def costumersCreate(request):
    form = CostumerForm()
    if request.method == 'POST':
        if request.FILES:
            if request.FILES['image']:
                form = CostumerForm(request.POST, request.FILES)
                if form.is_valid():
                    Instance = form.save()
                    costumerImage = str(Instance.image.url)
                    costumerImage = get_file_path(costumerImage)
                    predictions = get_prediction(image=costumerImage, model=model)[1]
                    Instance.prediction = predictions
                    Instance.save()
                    return redirect(costumersDetails, Instance.id)
        else:
            form = CostumerForm(request.POST)

        if form.is_valid():
            Instance = form.save()
            return redirect(costumersDetails, Instance.id)

    context = {
        'pageActive': 'Costumers',
        'CostumerForm': form,
    }
    return render(request, 'costumers/costumersCreate.html', context)

@login_required(login_url='authentification')
def costumersModify(request, id):
    costumer = Costumer.objects.get(id=id)
    form = CostumerForm(instance=costumer)
    if request.method == 'POST':
        if request.FILES:
            if request.FILES['image']:
                form = CostumerForm(request.POST, request.FILES, instance=costumer)
                if form.is_valid():
                    Instance = form.save()
                    costumerImage = str(Instance.image.url)
                    costumerImage = get_file_path(costumerImage)
                    predictions = get_prediction(image=costumerImage, model=model)[1]
                    Instance.prediction = predictions
                    Instance.save()
                    return redirect(costumersDetails, id)
        else:
            form = CostumerForm(request.POST, instance=costumer)

        if form.is_valid():
            form.save()
            return redirect(costumersDetails, id)

    context = {
        'pageActive': 'Costumers',
        'costumer': costumer,
        'CostumerForm': form,
    }
    return render(request, 'costumers/costumersModify.html', context)

@login_required(login_url='authentification')
def costumersDelete(request, id):
    costumer = Costumer.objects.get(id=id)
    costumer.delete()
    return redirect(costumersList)