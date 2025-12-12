from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider_list, name='provider_list'),
    path('add/', views.add_provider, name='add_provider'),
]