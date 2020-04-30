from django.shortcuts import render, redirect

from .models import *
from .forms import *

def home(request):
    dataset = Dataset.objects.all()
    context ={
        'dataset': dataset
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')



def create(request):
    form = DatasetForm()
    if request.method == "POST":
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    data = Dataset.objects.get(id=pk) # id
    form = DatasetForm(instance=data) # hare you can see you previous data.
    if request.method == "POST":
        form = DatasetForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()

    context = {
        'data': data,
        'form': form
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    data = Dataset.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('home')

    context = {
        'item': data
    }
    return render(request, 'delete.html', context)


