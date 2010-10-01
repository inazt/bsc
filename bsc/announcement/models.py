from django.contrib.auth.models import User
from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class News(Content):
    slug = models.SlugField(blank=True)
    class Meta:
        verbose_name_plural = 'News'


class Event(Content):
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=255, default='')
