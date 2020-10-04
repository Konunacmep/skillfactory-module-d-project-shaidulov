from django.db import models
from datetime import date

BOOL_CHOICES = ((True, 'Мальчик'), (False, 'Девочка'))

class Animal(models.Model):
    animal_type = models.CharField(max_length=20, verbose_name='Вид')

    def __str__(self):
        return self.animal_type

class Breed(models.Model):
    animal_type_ref = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Вид')
    breed_name = models.CharField(max_length=200, verbose_name='Порода')
    breed_description = models.TextField(null=True, blank=True, verbose_name='Характеристика породы')

    def __str__(self):
        return self.breed_name

class Pet(models.Model):
    animal_type_ref = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Вид')
    breed = models.ForeignKey(Breed, verbose_name='Порода', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.CharField(max_length=20, null=True, blank=True, verbose_name='Примерный возраст', help_text='Примеры заполнения: 1 год; 5 месяцев; 7 лет; 2 дня')
    gender = models.BooleanField(choices=BOOL_CHOICES, null=True, blank=True, default=True, verbose_name='Пол')
    story = models.TextField(null=True, blank=True, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата поступления')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    @property
    def time_here(self):
        return (date.today()-self.date).days
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/pet_default.png"
    def __str__(self):
        return f"{self.name}, {self.animal_type_ref}, {self.breed}"

