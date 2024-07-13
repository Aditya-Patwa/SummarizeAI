from django.shortcuts import render
import os

# Create your views here.

def summarize_webpage(request, href):
    return render(request, "index.html", {"content": "some_content"})