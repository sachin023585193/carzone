from django.shortcuts import redirect, render
from .models import contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            hasContacted = contact.objects.filter(car_id=car_id,user_id=user_id)
            if hasContacted:
                messages.error(request,'You have already made an enquiry about this car please wit till we get back to you')
                return redirect('/cars/'+car_id)
        admin_infos = User.objects.filter(is_superuser=True)
        admins_email = []
        for admin_info in admin_infos:
            admins_email.append(admin_info.email)
        send_mail(
            'New Car inquiry',
            'You have new inquiry for ' + car_title + ' please login to your admin pannel fo more info',
            'sachinbh023@gmail.com',
            admins_email,
            fail_silently=False,
        )
        add_contact = contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)
        add_contact.save()
        messages.success(request,'Your request has been submitted we will get back to you shortly')
        return redirect('/cars/'+car_id)

 