from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.

class Space(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    space_id = models.UUIDField(default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.name