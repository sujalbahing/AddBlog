from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','Title','Subtitle','Image','Description']