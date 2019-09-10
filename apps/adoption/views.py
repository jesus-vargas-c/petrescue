from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
app_name = 'adoption'

def index_adoption(request):
    return HttpResponse("This is the main page for adoption")
