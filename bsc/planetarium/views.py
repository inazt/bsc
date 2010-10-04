from django.shortcuts import render_to_response
from django.template import RequestContext

from bsc.planetarium.models import Post, Blog
from bsc.planetarium.forms import BlogPostForm

def post_display(request, blog_slug, post_id):
    post = Post.objects.get(id=post_id)
    ctx = RequestContext(request, {'post': post})
    return render_to_response('planetarium/post_display.html', ctx)

def post_new_form(request, blog_slug):
    f = BlogPostForm()
    ctx = RequestContext(request, {'form': f})
    return render_to_response('planetarium/post_new_form.html', ctx)
