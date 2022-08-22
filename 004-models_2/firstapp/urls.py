
from django.urls import path
from .views import firstapp,subfolder
urlpatterns = [
    path("",firstapp), # /firstapp
    path("subfolder/",subfolder), #/firstapp/subfolder
]
