from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from twitter_like.microblog.forms import TweetForm
from twitter_like.microblog.models import Tweet, MicroBlog

# from twitter_like.microblog.models import MicroBlog

@login_required
def index(request):
    if request.user:
        authen = "/accounts/logout?next=/"
    else:
        authen = "/accounts/login?next=/"
    f = TweetForm()
    all_tweets = Tweet.objects.all()
    tweets = all_tweets.order_by('-id').all()[:10]
    ctx = RequestContext(request, {'tweet_form': f.as_table(), 'tweets_list': tweets, 'count': all_tweets.count(), 'authen': authen})
    return render_to_response('microblog/index.html', ctx)

@login_required
def tweet_new(request, microblog):
    if (request.POST):
        f = TweetForm(request.POST)
        if f.is_valid():
            tweet = f.save(commit=False)
            microblog = MicroBlog.objects.get(slug=microblog)
            author = request.user
            tweet.microblog = microblog
            tweet.author = author
            tweet.save()
    
    return redirect('/')

@login_required
def tweet_delete(request, microblog, tweet_id):
    Tweet.objects.get(id=tweet_id).delete()
    return redirect('/')
