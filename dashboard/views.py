from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def summarize_youtube_video(request):
    pass


@login_required
def summarize_webpage(request):
    pass


@login_required
def summarize_documents(request):
    pass
