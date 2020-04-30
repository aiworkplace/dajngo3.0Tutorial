from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    dataset = Dataset.objects.all()
    context ={
        'dataset': dataset
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')