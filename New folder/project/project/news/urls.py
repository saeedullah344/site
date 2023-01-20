from django.contrib import admin
from django.urls import path, include
from news import views
urlpatterns = [
path('news',views.news,name='news'),
path('news/<newsid>',views.detail,name='Detail')

]
