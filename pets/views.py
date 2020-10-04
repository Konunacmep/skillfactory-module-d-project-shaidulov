from django.shortcuts import render
from .models import Pet, Animal, Breed
from django.views.generic import TemplateView
from django.db.models import F, Max
from random import randint
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import PetForm, BreedForm
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.

def getbreedlist(request, breed_id):
    if breed_id != 0:
        res = list(Breed.objects.all().filter(animal_type_ref=breed_id).values())
    else:
        res = list(Breed.objects.all().values())
    return JsonResponse(res, safe=False)

class Landing(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount'] = Pet.objects.count()
        if context['amount'] > 0:
            max_id = Pet.objects.all().aggregate(max_id=Max("id"))['max_id']
            item=None
            while True:
                pk = randint(1, max_id)
                item = Pet.objects.filter(pk=pk).first()
                if item:
                    break
            context['random_card'] = item
        return context

class AddPet(CreateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pets:pet_list')
    template_name = 'pet_edit.html'

class EditPet(UpdateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pets:pet_list')
    template_name = 'pet_edit.html'

class PetList(ListView):
    template_name = 'pet_list.html'
    context_object_name = 'pets'
    model = Pet

class AddBreed(CreateView):
    model = Breed
    form_class = BreedForm
    success_url = reverse_lazy('pets:add_pet')
    template_name = 'breed_edit.html'

class PetDetail(DeleteView):
    model = Pet
    template_name = 'pet.html'
    context_object_name = 'pet'
