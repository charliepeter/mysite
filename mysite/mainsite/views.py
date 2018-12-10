from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import TestPost

# Create your views here.

def index(request):
    return render(request, 'mainsite/index.html')

def photo(request):
    post = TestPost.objects.all()
    post = {'post':post}
    return render(request, 'mainsite/photo.html', post)

def photo_post(request, slug):
    return HttpResponse(slug)

def video(request):
    return render(request, 'mainsite/video.html')

def video_post(request, slug):
    return HttpResponse(slug)

def writing(request):
    return render(request, 'mainsite/writing.html')

def writing_post(request, slug):
    return HttpResponse(slug)

def diary(request):
    return render(request, 'mainsite/diary.html')

def diary_post(request, slug):
    return HttpResponse(slug)

def about(request):
    return render(request, 'mainsite/about.html')