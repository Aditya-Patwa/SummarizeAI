from django.contrib import admin
from .models import YoutubeVideoSummary, WebpageSummary

# Register your models here.
admin.site.register(YoutubeVideoSummary)
admin.site.register(WebpageSummary)