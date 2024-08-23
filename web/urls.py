from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='home'),
    path ('acerca/', views.about, name='acerca'),
    path ('bienvenido/', views.welcome, name='bienvenido'),
    path ('contacto/', views.contacto, name='contacto'),
    path ('exito/', views.success, name='exito'),
]