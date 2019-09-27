from django.conf.urls import url, include
from apps.pet.views import index, pet_view, pet_list, pet_edit, pet_delete


app_name='pet'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', pet_view, name='pet_create'),
    url(r'^list$', pet_list, name='pet_list'),
    url(r'^edit/(?P<id_pet>\d+)/$', pet_edit, name='pet_edit'),
    url(r'^delete/(?P<id_pet>\d+)/$', pet_delete, name='pet_delete'),



]
