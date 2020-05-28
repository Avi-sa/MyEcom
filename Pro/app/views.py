from django.shortcuts import render
from app.models import Product

def home(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'products/home.html',context)
# Create your views here.
