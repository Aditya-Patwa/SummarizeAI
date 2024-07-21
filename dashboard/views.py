from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import Summary
# Create your views here.

@login_required
def Dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def summarize_youtube_video(request):
    if request.method == "POST":
        videolink = request.POST.get("videolink")
    return render(request, "dashboard/products/summarize_youtube_video.html")


@login_required
def summarize_webpage(request):
    if request.method == "POST":
        webpage_link = request.POST.get("webpage_link")
    return render(request, "dashboard/products/summarize_webpage.html")


@login_required
def summarize_document(request):
    if request.method == "POST":
        uploaded_document = request.FILES['uploaded_document']
        print(uploaded_document.open())
    return render(request, "dashboard/products/summarize_document.html")


@login_required
def view_summary(request, summary_id):
    return render(request, "dashboard/summary.html")