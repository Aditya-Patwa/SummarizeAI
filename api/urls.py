from django.urls import path
from . import views

urlpatterns = [
    path("<str:href>", views.summarize_webpage, name="summarize webpage"),
]