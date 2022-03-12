from django.contrib import admin
from .models import contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','car_title','city')
    list_display_links = ('id','first_name')
    search_fields = ('first_name','last_name','id','car_title')
    list_per_page=25

# Register your models here.
admin.site.register(contact,ContactAdmin)