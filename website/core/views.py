from django.shortcuts import render
from store.models import Product


def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:8]
    return render(request, 'core/frontpage.html', {
        'products': products
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