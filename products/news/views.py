from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, generics
from .models import Products

def news_home(request):
    product = Products.objects.all()
    return render(request, 'news/news_home.html',{'product':product})
    permissions_classes = [permissions.IsAuthenticated]
  