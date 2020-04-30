from django.forms import ModelForm
from django import forms

from .models import *


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = '__all__'          #['age', 'name']