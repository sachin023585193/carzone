from django.contrib import messages,auth
from django.shortcuts import redirect, render

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
        messages.error(request,'this is error message')
        return redirect('login')
    else:
        return render(request,'account/register.html')

def dashboard(request):
    return render(request,'account/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logout Successfully')
    return redirect('home')