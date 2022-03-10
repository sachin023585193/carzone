from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cars',views.cars,name='cars'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]