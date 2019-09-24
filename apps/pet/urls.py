from django.conf.urls import url, include
from apps.pet.views import index

app_name='pet'

urlpatterns = [
    url(r'^$', index, name='index'),
]
