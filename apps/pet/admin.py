from django.contrib import admin

from apps.pet.models import Vaccine, Pet

# Register your models here.

admin.site.register(Vaccine)
admin.site.register(Pet)
