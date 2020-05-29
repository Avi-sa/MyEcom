from django.shortcuts import render
from app.models import Product

def home(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'products/home.html',context)

def all(request):
    product = Product.objects.all()
    context = {'product':product}
    return reverse(request,'products/all.html',context)
# Create your views here.
