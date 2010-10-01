from django.shortcuts import render_to_response
from django.template import RequestContext

from bsc.planetarium.models import Post, Blog

def post_display(request, blog_slug, post_id):
    post = Post.objects.get(id=post_id)
    ctx = RequestContext(request, {'post': post})
    return render_to_response('planetarium/post_display.html', ctx)
