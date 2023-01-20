from django.contrib import admin
from django.urls import path
from myproject import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('form', views.form, name='form'),
    path('saeed', views.saeed, name='saeed'),
    path('sheet', views.sheet, name='sheet'),
    path('blog/<slug:detail>', views.blogdetail, name='blogdetail')
]   
