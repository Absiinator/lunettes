from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .getPredictions import *
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import pickle

# loading model on server start
BASE_DIR = Path(__file__).resolve().parent.parent
model = pickle.load(open(f'{BASE_DIR}/lunettes/static/AI/model.pkl', 'rb'))

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
    declared_gender = str(costumer.gender)

    context = {
        'pageActive': 'Costumers',
        'costumer': costumer,
        'declared_genre': declared_gender # this is needed in order to compare string to string values in template
    }
    return render(request, 'costumers/costumersDetails.html', context)

def costumersCreate(request):
    form = CostumerForm()
    if request.method == 'POST':
        if request.FILES:
            if request.FILES['image']:
                form = CostumerForm(request.POST, request.FILES)
                if form.is_valid():
                    Instance = form.save(commit=False)
                    costumerImage = str(Instance.image.url)
                    predictions = get_prediction(image=costumerImage, model=model)[1]
                    Instance.prediction = predictions
                    Instance.save()
        else:
            form = CostumerForm(request.POST)

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