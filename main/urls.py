from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("products/", views.Products, name="products"),
]