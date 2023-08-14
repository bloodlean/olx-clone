from django.shortcuts import render, get_object_or_404           
from .models import Product
from .models import Transport
from .models import Furniture
from .models import Cloth
from .models import Sport
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')

def electronics(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(
        request,
        'pages/electronics.html',
        context
    )

@login_required(redirect_field_name='login')
def sale_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product': product
    }
    return render(request, 'pages/sale_detail.html', context)

def transport(request):
    transports = Transport.objects.all()
    context = {
        'transports':transports
    }
    return render(request, 'pages/transport.html', context)

@login_required(redirect_field_name='login')
def transport_detail(request, pk):
    try:
        transport = Transport.objects.get(id=pk)
    except Transport.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'transport': transport
    }
    return render(request, 'pages/transport_detail.html', context)



def furniture(request):
    furnitures = Furniture.objects.all()
    context = {
        'furnitures': furnitures
    }
    return render(request, 'pages/furniture.html', context)

@login_required(redirect_field_name='login')
def furniture_detail(request, pk):
    try:
        furnitures = Furniture.objects.get(id=pk)
    except Furniture.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'furnitures': furnitures
    }
    return render(request, 'pages/furniture_detail.html', context)



def clothes(request):
    clothes = Cloth.objects.all()
    context = {
        'clothes': clothes
    }
    return render(request, 'pages/clothes.html', context)

@login_required(redirect_field_name='login')
def clothes_detail(request, pk):
    try:
        cloth = Cloth.objects.get(id=pk)
    except Cloth.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'cloth': cloth
    }
    return render(request, 'pages/clothes_detail.html', context)


def sport(request):
    sport = Sport.objects.all()
    context = {
        'sport': sport
    }
    return render(request, 'pages/sport.html', context)

@login_required(redirect_field_name='login')
def sport_detail(request, pk):
    try:
        sports = Sport.objects.get(id=pk)
    except Sport.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'sports': sports
    }
    return render(request, 'pages/sport_detail.html',context)
