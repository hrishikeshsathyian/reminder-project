from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.
#home page when first entering site

def base(request):
    return render(request,'home/base.html')
# Create a new user in the database
def signupuser(request):
    if request.method == 'GET':
        return render(request,'home/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'],password = request.POST['password1'], email=None)
                user.save()
                login(request,user)
                return redirect('current')
            except IntegrityError:
                return render(request,'home/signupuser.html',{'form':UserCreationForm(), 'error2':'User Already Taken'})
        else:
            return render(request,'home/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords do not match :('})
def loginuser(request):
    if request.method == 'GET':
        return render(request,'home/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username = request.POST['username'],password= request.POST['password'])
        if user is None:
            return render(request,'home/loginuser.html',{'form':AuthenticationForm(), 'error': 'either your password is wrong or your account doesnt exist im lazy isolate it for you'})
        else:
            login(request,user)
            return redirect('current')
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('base')
