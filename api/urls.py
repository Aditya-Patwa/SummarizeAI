from django.urls import path
from . import views


urlpatterns = [
    path("summarize_webpage/", views.summarize_webpage, name="summarize webpage"),
    path("ask_question/", views.ask_question, name="ask question")
]