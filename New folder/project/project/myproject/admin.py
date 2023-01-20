from django.contrib import admin
from myproject.models import service

# Register your models here.

class Services(admin.ModelAdmin):
    list_display = ('name','fname','mesage') 


admin.site.register(service,Services)
