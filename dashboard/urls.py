from django.urls import path
from . import views

urlpatterns = [
    path("", views.Dashboard, name="Dashboard"),
    path("summarize/webpage/", views.summarize_webpage, name="summarize_webpage"),
    path("summarize/youtube/", views.summarize_youtube_video, name="summarize_youtube_video"),
    path("summarize/document/", views.summarize_document, name="summarize_document"),
    path("summary/webpage/<str:summary_id>", views.view_webpage_summary, name="view_summary"),
    path("summary/youtube/<str:summary_id>", views.view_youtube_summary, name="view_summary"),
]