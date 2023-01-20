from django.shortcuts import render,HttpResponse
from news import urls
from news.models import NEWS
# Create your views here.

def news(request):
    newApp=NEWS.objects.all()
    data={
        'newsapp':newApp
    }
    return render(request,'news.html',data)


def detail(request,newsid):
    newsDetail = NEWS.objects.get(id=newsid)
    newskhan={
        'newssaed':newsDetail
    }
    return render(request,'newsdetail.html',newskhan)
