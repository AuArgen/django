from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def news_home(request):
    return render(request, 'news/news_home.html')