from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import entries

def home(request):
	Entries = entries.object.order_by('-id')[:3]
	return HttpResponse("hello")

def archive(request):
	return HttpResponse("hello, archive")
		
def about(request):
	return HttpResponse("hello, about")

def test(request):
	return HttpResponse("hello, test")
