from django.contrib import admin
from news.models import NEWS
# Register your models here.

class News(admin.ModelAdmin):
    list_display= ('news_title','news_desc')
admin.site.register(NEWS,News)
