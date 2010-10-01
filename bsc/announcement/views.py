from django.shortcuts import render_to_response
from django.template import RequestContext

from bsc.announcement.models import News, Event

def news_list(request):
    news = News.objects.all()[:10]
    ctx = RequestContext(request, {'news_list': news})
    return render_to_response('announcement/news_list.html', ctx)
    

def news_display(request, nid):
    news = News.objects.get(id=nid)
    ctx = RequestContext(request, {'news': news})
    return render_to_response('announcement/news_display.html', ctx)
    

def event_list(request):
    event = Event.objects.all()[:10]
    ctx = RequestContext(request, {'event_list': event})
    return render_to_response('announcement/event_list.html', ctx)
    

def event_display(request, nid):
    event = Event.objects.get(id=nid)
    ctx = RequestContext(request, {'event': event})
    return render_to_response('announcement/event_display.html', ctx)
    
