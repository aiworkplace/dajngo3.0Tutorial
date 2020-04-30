from django.forms import ModelForm

from .models import *


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = '__all__'          #['age', 'name']
