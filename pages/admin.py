from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamCustom(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width="40" style="border-radius:50%" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    
    list_display = ('id','thumbnail','first_name','designation','created_date')
    list_display_links = ('id','first_name',)
    search_fields = ('first_name','last_name')
    list_filter = ('designation',)

# Register your models here.
admin.site.register(Team,TeamCustom)