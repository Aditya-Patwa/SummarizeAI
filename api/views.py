from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os

# Create your views here.
# from langchain.chains.summarize import load_summarize_chain
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_huggingface import ChatHuggingFace
# from langchain_huggingface import HuggingFaceEndpoint

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     task="text-generation",
#     max_new_tokens=512,
#     do_sample=False,
#     repetition_penalty=1.03,
# )



def summarize_webpage(request):
    requested_web_url = request.body.decode("utf-8")

    return JsonResponse({"web_url": requested_web_url})