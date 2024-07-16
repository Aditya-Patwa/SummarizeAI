from django.contrib import admin
from .models import Summary, YoutubeVideoSummary, WebPageSummary

# Register your models here.
admin.site.register(Summary)
admin.site.register(YoutubeVideoSummary)
admin.site.register(WebPageSummary)