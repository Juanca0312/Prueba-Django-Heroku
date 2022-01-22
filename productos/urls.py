from unicodedata import name
from django.urls import path

from productos import views

urlpatterns = [
    path('productos', views.ProductosView.as_view(), name='productos')
]