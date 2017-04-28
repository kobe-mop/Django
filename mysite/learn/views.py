from django.shortcuts import render

# Create your views here.
#coding:utf-8
from django.http import HttpResponse
from .models import Blog
 


def home(request):
    return render(request, 'home.html')

def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)