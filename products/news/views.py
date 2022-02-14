from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


# Create your views here.

def news_home(request):
    product = Products.objects.all()
    return render(request, 'news/news_home.html',{'product':product})