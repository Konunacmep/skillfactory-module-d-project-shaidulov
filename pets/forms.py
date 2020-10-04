from django import forms
from .models import Pet, Animal, Breed

class DateInput(forms.DateInput):
     input_type = 'date'

class PetForm(forms.ModelForm):
    class Meta:
        widgets = {'date':DateInput()}
        model = Pet
        fields = '__all__'

class BreedForm(forms.ModelForm):
    class Meta:
        model =  Breed
        fields = '__all__'
