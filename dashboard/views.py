from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from api.models import WebpageSummary, YoutubeVideoSummary
from django.core.files.storage import FileSystemStorage
from .helper import load_web_page, load_youtube_video, load_document
from langchain_community.document_loaders import YoutubeLoader
# Create your views here.

@login_required
def Dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def summarize_youtube_video(request):
    if request.method == "POST":
        videolink = request.POST.get("videolink")
        video_id = YoutubeLoader.extract_video_id(videolink)
        try:
            youtube = YoutubeVideoSummary.objects.get(video_id=video_id, user=request.user)
            return redirect(f"/dashboard/summary/youtube/{youtube.summary_id}")
        except:
            (response, youtube_summary_id) = load_youtube_video(videolink, request.user)
            return redirect(f"/dashboard/summary/youtube/{youtube_summary_id}")
    return render(request, "dashboard/products/summarize_youtube_video.html")


@login_required
def summarize_webpage(request):
    if request.method == "POST":
        webpage_link = request.POST.get("webpage_link")
        try:
            webpage = WebpageSummary.objects.get(link=webpage_link, user=request.user)
            return redirect(f"/dashboard/summary/webpage/{webpage.summary_id}")
        except:
            (response, webpage_summary_id) = load_web_page(webpage_link, request.user)
            return redirect(f"/dashboard/summary/webpage/{webpage_summary_id}")
    return render(request, "dashboard/products/summarize_webpage.html")


@login_required
def summarize_document(request):
    if request.method == "POST":
        f = request.FILES['uploaded_document']
        fs = FileSystemStorage()
        filename = str(f)
        file = fs.save(f"document/{filename}", f)
        fileurl = fs.url(file)
        print(fileurl)
        load_document(fileurl, request.user)
    return render(request, "dashboard/products/summarize_document.html")


@login_required
def view_webpage_summary(request, summary_id):
    try:
        summary = WebpageSummary.objects.get(user=request.user, summary_id=summary_id)
    except WebpageSummary.DoesNotExist:
        return HttpResponseNotFound("Summary Not Found!")
    return render(request, "dashboard/summary/webpage.html", { "summary": summary })


@login_required
def view_youtube_summary(request, summary_id):
    try:
        summary = YoutubeVideoSummary.objects.get(user=request.user, summary_id=summary_id)
    except WebpageSummary.DoesNotExist:
        return HttpResponseNotFound("Summary Not Found!")
    return render(request, "dashboard/summary/youtube.html", { "summary": summary })