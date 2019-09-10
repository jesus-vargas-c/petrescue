from django.conf.urls import url, include
from apps.pet.views import index_pet

app_name='pet'

urlpatterns = [
    url(r'^index$', index_pet),
]
