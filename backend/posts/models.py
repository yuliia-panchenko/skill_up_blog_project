"""
Post:
id: int
title: str
content: str
author_id: int

User:
id: int
username: str
first_name: str
last_name: str
password: str
"""

from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
