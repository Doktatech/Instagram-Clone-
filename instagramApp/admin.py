from django.contrib import admin
from .models import Photo,caption
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('caption')

    admin.site.register(Photo)
    admin.site.register(caption)