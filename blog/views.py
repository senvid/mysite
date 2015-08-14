from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from blog.models import entries
import json

# def home(request):
#   Entries = entries.objects.order_by('-id')[:3]
#   templ = loader.get_template('home.html')
#   contex = RequestContext(request,{'Entries':Entries})
#   return HttpResponse(templ.render(contex))

# another way


def home(request):
    Entries = entries.objects.order_by('-id')[:3]
    return render(request, "home.html", {'Entries': Entries})


def entry(request, entries_slug):
    try:
        article = entries.objects.filter(slug=entries_slug)
    except Exception:
        raise Http404("Nothing here.")
    return render(request, "home.html", {'Entries': article})

def aside(request):
    try:
        aside_title = entries.objects.order_by('-id')[:6].values('title','slug')
    except Exception:
        raise Http404("Nothing here")
    #return HttpResponse(json.dumps(list(aside_title)), content_type="application/json")
    return HttpResponse(json.dumps(list(aside_title)))

def archive(request):
    return HttpResponse("hello, archive")


def about(request):
    return HttpResponse("hello, about")


def test(request):
    return HttpResponse("hello, test")
