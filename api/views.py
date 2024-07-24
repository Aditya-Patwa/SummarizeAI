from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import json
from dashboard.helper import answer_question

# Create your views here.

def summarize_webpage(request):
    requested_web_url = request.body.decode("utf-8")

    return JsonResponse({"web_url": requested_web_url})

def ask_question(request):
    try:
        params = json.loads(request.body)
        question = params["question"]
        summaryid = params["summaryid"]

        answer = answer_question(request.user, summaryid, question)
        print(answer)
        return JsonResponse({"status": "success", "answer": answer})
    except:
        return JsonResponse({"status": "error"})