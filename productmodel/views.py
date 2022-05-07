from django.http import HttpResponse
from matplotlib.style import context
from .models import *
from django.shortcuts import render
from .forms import productmanagement

def home(request):
    return HttpResponse("hi homie")

def MyProduct(request):
    products = product.objects.all()
    context = {
        "products":products,

    }
    print (products)
    return render(request,"index.html",context)    

def productForm (request):
    context={}
    form = productmanagement(request.POST or None,request.FILES or None)
    if form.is_valid:
        form.save()

    context["form"]=form
    return render(request,"forms.html",context)
