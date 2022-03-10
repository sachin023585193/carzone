from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class carAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width="50" style="border-radius:12px" />'.format(object.car_photo1.url))
    thumbnail.short_description = 'Photo'
    
    list_display = ('id','car_title','thumbnail','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links = ('id','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','city')
    list_filter=('city','fuel_type')

# Register your models here.
admin.site.register(Car,carAdmin)