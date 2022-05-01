from django import views
from django.urls import path
from familiares import views

urlpatterns = [
    path('', views.vistafamiliares, name='home'),
]