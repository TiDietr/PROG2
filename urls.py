from django.urls import path
from . import views

urlpatterns= [
path('bestaetigung.html', views.bestaetigung, name="bestaetigung"),
]