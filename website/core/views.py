from django.shortcuts import render
from django.contrib.auth.models import User
from store.models import Category, Product


def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:8]
    return render(request, 'core/frontpage.html', {
        'products': products,
        'product_count': Product.objects.filter(status=Product.ACTIVE).count(),
        'category_count': Category.objects.count(),
        'seller_count': User.objects.filter(products__status=Product.ACTIVE).distinct().count(),
    })

def help(request):
    return render(request, 'core/help.html')

def sell(request):
    return render(request, 'core/sell.html')

def signup(request):
    return render(request, 'userprofile/signup.html')

def logout(request):
    return render(request, 'core/frontpage.html')

def login(request):
    return render(request, 'userprofile/login.html')

def shoppingcart(request):
    return render(request, 'core/shoppingcart.html')
