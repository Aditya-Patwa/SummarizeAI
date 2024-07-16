from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Space
from datetime import datetime
import uuid

# Create your models here.

class Summary(models.Model):
    name = models.CharField(max_length=250)
    summary = models.JSONField(null=True, blank=True)
    vectorstore = models.JSONField(null=True, blank=True)
    question_answers = models.JSONField(null=True, blank=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Summary: {self.name}"


class YoutubeVideoSummary(Summary):
    video_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Youtube Summary of Id: {video_id}"


class WebPageSummary(Summary):
    link = models.TextField()

    def __str__(self):
        return f"Website Summary: {self.link}"


# class SummarizeYoutubeVideo(models.Model):
#     video_name = models.CharField(max_length=250)
#     video_id = models.CharField(max_length=100)
#     summary = models.JSONField(null=True, blank=True)
#     vectorstore = models.JSONField(null=True, blank=True)
#     question_answers = models.JSONField(null=True, blank=True)

#     class Meta:
#         ordering = ["-created_at"]

#     def __str__(self):
#         return f"Youtube Video Summarization of Id: {self.video_id}"


# class SummarizeWebPage(models.Model):
#     link_name = models.CharField(max_length=250)
#     url = models.TextField(null=True, blank=True)
#     summary = models.JSONField(null=True, blank=True)
#     vectorstore = models.JSONField(null=True, blank=True)
#     question_answers = models.JSONField(null=True, blank=True)
#     space = models.ForeignKey(Space, on_delete=models.CASCADE)
#     summary_id = models.UUIDField(default=uuid.uuid4, editable=False)
#     created_at = models.DateTimeField(default=datetime.now)
    
#     class Meta:
#         ordering = ["-created_at"]

#     def __str__(self):
#         return f"Webpage Summary: {self.link_name}"
