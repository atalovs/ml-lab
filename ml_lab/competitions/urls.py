# competitions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.competitions, name='competitions'),
]