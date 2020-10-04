from django.urls import path
from .views import Landing, AddPet, getbreedlist, PetList, AddBreed, PetDetail, EditPet

app_name = 'pets'
urlpatterns = [
    path('add', AddPet.as_view(), name='add_pet'),
    path('getbreedlist/<int:breed_id>', getbreedlist, name='breedlist'),
    path('petlist', PetList.as_view(), name='pet_list'),
    path('addbreed', AddBreed.as_view(), name='add_breed'),
    path('petdetail/<int:pk>', PetDetail.as_view(), name='pet_detail'),
    path('petedit/<int:pk>', EditPet.as_view(), name='pet_edit'),
    ]