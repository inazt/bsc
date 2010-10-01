from django.contrib.auth.models import User
from django.db import models

class Loggable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(Loggable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Post(Loggable):
    blog = models.ForeignKey('Blog')
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
