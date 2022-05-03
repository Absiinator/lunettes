from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Products views
def productList(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'pageActive': 'Products',
        'products': products,
        'categories': categories,
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


# Categories views
def categoriesCreate(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(productList)

    context = {'pageActive': 'Products',
               'CategoryForm': form}
    return render(request, './products/categoriesCreate.html', context)

def categoriesDetails(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    context = {'pageActive': 'Products',
                'products': products,
                'category': category}
    return render(request, './products/categoriesDetails.html', context)

def categoriesModify(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(categoriesDetails, id)

    context = {'pageActive': 'Products',
               'category': category,
               'CategoryForm': form}
    return render(request, './products/categoriesModify.html', context)

def categoriesDelete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(productList)