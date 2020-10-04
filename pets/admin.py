from django.contrib import admin
from .models import Pet, Breed, Animal

# Register your models here.
@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass