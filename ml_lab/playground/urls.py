from django.urls import path
from . import views

urlpatterns = [
    path('', views.playground, name='playground'),
]
