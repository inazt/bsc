from django.shortcuts import render_to_response
from django.template import RequestContext

from bsc.news.models import News

def index(request):
    latest_news = News.objects.all()[:10]
    context = RequestContext(request, {'latest_news': [latest_news[:5], latest_news[5:10]]})
    return render_to_response('homepage/index.html', context)
