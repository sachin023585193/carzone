from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from contacts.models import contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Login successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    return render(request,'account/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    auth.login(request,user)
                    messages.success(request,'You are registered successfully')
                    return redirect('dashboard')
        else:
            messages.error(request,'Password donot match')
        return redirect('register')
    else:
        return render(request,'account/register.html')

@login_required(login_url='login')
def dashboard(request):
    user_inquiry = contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    context = {'inquiries':user_inquiry}
    return render(request,'account/dashboard.html',context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logout Successfully')
    return redirect('home')