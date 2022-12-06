from django.forms import ModelForm
from .models import *


class PersonFitnessForm(ModelForm):
    class Meta:
        model = PersonFitness
        fields = '__all__'
        
        
        
 
    