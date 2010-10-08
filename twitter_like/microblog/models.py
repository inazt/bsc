from django.contrib.auth.models import User
from django.db import models

class Loggable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MicroBlog(Loggable):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name


class Tweet(Loggable):
    microblog = models.ForeignKey('MicroBlog')
    message = models.TextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.message
