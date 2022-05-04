from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Products views
@login_required(login_url='authentification')
def productList(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'pageActive': 'Products',
        'products': products,
        'categories': categories,
        }
    return render(request, 'products/products.html', context)

@login_required(login_url='authentification')
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

@login_required(login_url='authentification')
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

@login_required(login_url='authentification')
def productsDetails(request, id):
    product = Product.objects.get(id=id)
    context = {'pageActive': 'Products',
               'product': product}
    return render(request, './products/productsDetails.html', context)

@login_required(login_url='authentification')
def productsDelete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(productList)


# Categories views
@login_required(login_url='authentification')
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

@login_required(login_url='authentification')
def categoriesDetails(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    context = {'pageActive': 'Products',
                'products': products,
                'category': category}
    return render(request, './products/categoriesDetails.html', context)

@login_required(login_url='authentification')
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

@login_required(login_url='authentification')    
def categoriesDelete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(productList)