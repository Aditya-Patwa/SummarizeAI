from django.urls import path
from . import views

urlpatterns = [
    path("", views.Dashboard, name="Dashboard"),
    path("summarize/webpage/", views.summarize_webpage, name="summarize_webpage"),
]