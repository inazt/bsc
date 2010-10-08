from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bsc.planetarium.models import Post, Blog
from bsc.planetarium.forms import BlogPostForm

def post_display(request, blog_slug, post_id):
    post = Post.objects.get(id=post_id)
    ctx = RequestContext(request, {'post': post})
    return render_to_response('planetarium/post_display.html', ctx)

@login_required
def post_new_form(request, blog_slug):
    if not request.user.is_authenticated():
        messages.error(request, 'Please log in first.')
        return redirect('/')

    if request.method == 'POST':
        f = BlogPostForm(request.POST)
        if f.is_valid():
            post = f.save(commit=False)
            blog = Blog.objects.get(slug=blog_slug)
            author = request.user
            post.blog = blog
            post.author = author
            post.save()
            messages.add_message(request, messages.INFO, 'New post has been saved.')
            return redirect('/blogs/'+ blog_slug +'/posts/'+ str(post.id))
    else:
        f = BlogPostForm()

    ctx = RequestContext(request, {'form': f.as_table(), 'blog_slug': blog_slug})
    return render_to_response('planetarium/post_new_form.html', ctx)

@login_required
def post_edit_form(request, blog_slug, post_id):
    if not request.user.is_authenticated():
        return redirect('/accounts/login/?next=/blogs/'+blog_slug+'/posts/'+str(post_id)+'/edit/')

    print request.user

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        f = BlogPostForm(request.POST, instance=post)
        if f.is_valid():
            post = f.save()
            messages.add_message(request, messages.INFO, 'This post has been saved.')
            return redirect('/blogs/'+ blog_slug +'/posts/'+ post_id)
    else:
        post = Post.objects.get(id=post_id)
        f = BlogPostForm(instance=post)

    ctx = RequestContext(request, {'form': f.as_table(), 'blog_slug': blog_slug, 'post_id': post_id})
    return render_to_response('planetarium/post_edit_form.html', ctx)
