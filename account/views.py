from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
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
    return redirect('home')