from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os

# Create your views here.

def summarize_webpage(request):
    requested_web_url = request.body.decode("utf-8")

    return JsonResponse({"web_url": requested_web_url})