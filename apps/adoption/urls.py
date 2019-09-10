from django.conf.urls import url 
from apps.adoption.views import index_adoption

app_name='adoption'
urlpatterns = [
    url(r'^index$', index_adoption)
]