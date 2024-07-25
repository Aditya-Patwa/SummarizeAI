from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from api.models import WebpageSummary, YoutubeVideoSummary
from django.core.files.storage import FileSystemStorage
from .helper import load_web_page, load_youtube_video, load_document
from langchain_community.document_loaders import YoutubeLoader
from celery.result import AsyncResult
# Create your views here.

@login_required
def Dashboard(request):
    youtubevideos = YoutubeVideoSummary.objects.filter(user=request.user)[0:5]
    webpage_summaries = WebpageSummary.objects.filter(user=request.user)[0:5]
    return render(request, "dashboard/dashboard.html", {"youtube_videos": youtubevideos, "webpage_summaries": webpage_summaries})


@login_required
def summarize_youtube_video(request):
    if request.method == "POST":
        videolink = request.POST.get("videolink")
        video_id = YoutubeLoader.extract_video_id(videolink)
        try:
            youtube = YoutubeVideoSummary.objects.get(video_id=video_id, user=request.user)
            return redirect(f"/dashboard/summary/youtube/{youtube.summary_id}")
        except:
            result = load_youtube_video.delay(videolink, request.user.id)
            youtube_summary_id = result.get()
            return redirect(f"/dashboard/summary/loading/{result.id}/type/youtube")
    summaries = YoutubeVideoSummary.objects.filter(user=request.user)
    return render(request, "dashboard/products/summarize_youtube_video.html", {"summaries": summaries})


@login_required
def summarize_webpage(request):
    if request.method == "POST":
        webpage_link = request.POST.get("webpage_link")
        try:
            webpage = WebpageSummary.objects.get(link=webpage_link, user=request.user)
            return redirect(f"/dashboard/summary/webpage/{webpage.summary_id}")
        except:
            result = load_web_page.delay(webpage_link, request.user.id)
            webpage_summary_id = result.get()
            return redirect(f"/dashboard/summary/loading/{result.id}/type/webpage")
    summaries = WebpageSummary.objects.filter(user=request.user)
    return render(request, "dashboard/products/summarize_webpage.html", {"summaries": summaries})


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
        summaries = summary.summary.split("\n")
    except WebpageSummary.DoesNotExist:
        return HttpResponseNotFound("Summary Not Found!")
    return render(request, "dashboard/summary/webpage.html", { "summary": summary, "summaries": summaries })


@login_required
def view_youtube_summary(request, summary_id):
    try:
        summary = YoutubeVideoSummary.objects.get(user=request.user, summary_id=summary_id)
        summaries = summary.summary.split("\n")
    except WebpageSummary.DoesNotExist:
        return HttpResponseNotFound("Summary Not Found!")
    return render(request, "dashboard/summary/youtube.html", { "summary": summary, "summaries": summaries })


@login_required
def loading(request, loading_id, site_type):
    return render(request, "dashboard/loading.html", {"loadingid": loading_id, "site_type": site_type})

def get_loading(request, loading_id):
    result = AsyncResult(loading_id)
    if result.status == "SUCCESS":
        return JsonResponse({"status": result.status, "id": result.get()})
    
    if result.status == "FAILURE":
        return JsonResponse({"status": result.status})
    return JsonResponse({"status": result.status})