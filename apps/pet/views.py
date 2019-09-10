from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
app_name='pet'

def index_pet(request):
    return HttpResponse("Index")
