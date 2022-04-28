from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def productList(request):
    products = Product.objects.all()
    context = {
        'pageActive': 'Products',
        'products': products
        }
    return render(request, 'products/products.html', context)

def productsCreate(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(productList)

    context = {'pageActive': 'Products',
               'ProductForm': form}
    return render(request, './products/productsCreate.html', context)

def productsModify(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(productsDetails, id)

    context = {'pageActive': 'Products',
                'product': product,
               'ProductForm': form}
    return render(request, './products/productsModify.html', context)

def productsDetails(request, id):
    product = Product.objects.get(id=id)
    context = {'pageActive': 'Products',
               'product': product}
    return render(request, './products/productsDetails.html', context)

def productsDelete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(productList)
