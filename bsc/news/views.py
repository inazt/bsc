from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers

from bsc.news.models import News

perpage = 5

def news_list(request):
    news = News.objects.all()[:perpage]
    return render_to_response('homepage/index.html', {'news': news})
    
def get_news(request):
    page = request.GET.get('page') or 0
    start = int(page) * perpage
    end = start + perpage
    news = News.objects.all()[start:end]
    return HttpResponse(serializers.serialize('json', news))
