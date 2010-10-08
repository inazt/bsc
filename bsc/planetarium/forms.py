from django.forms import ModelForm 

from bsc.planetarium.models import Post

class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug']
