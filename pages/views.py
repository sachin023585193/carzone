from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from cars.models import Car
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    context = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        }
    return render(request,'pages/home.html',context)

def about(request): 
    teams = Team.objects.all()
    context = {'teams':teams,}
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html')

def cars(request):
    return render(request,'pages/cars.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_infos = User.objects.filter(is_superuser=True)
        admins_email = []
        for admin_info in admin_infos:
            admins_email.append(admin_info.email)
        send_mail(
            'You have new contact mail regarding '+subject,
            'Name: ' + name + 'Email: ' + email + 'Phone: ' + phone + 'Message: ' + message,
            'sachinbh023@gmail.com',
            admins_email,
            fail_silently=False,
        )
        messages.success(request,'Thank you cor contacting us we will contact you shortly')
        return redirect('contact')
    return render(request,'pages/contact.html')