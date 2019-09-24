from django.shortcuts import render
from django.http import HttpResponse

from apps.pet.forms import PetForm
# Create your views here.
app_name='pet'

def index(request):
    return render(request, 'pet/index.html')

def pet_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.isValid():
            form.save()
        return redirect('pet:index')