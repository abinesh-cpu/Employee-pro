from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')
# Create your views here.

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(userhome)
        else:
            return redirect(userlogin)
    return render(request,'userlogin.html')
def userregister(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        data=User.objects.create_user(username=email,email=email,password=password,first_name=username)
        data.save()
        return redirect(userlogin)
    return render(request,'userregister.html')

adminusername="abi123"
adminpassword="abi@123"
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adminusername and password==adminpassword:
            print("logged in")
            request.session['adm']=adminusername
            return redirect(adminhome)
    return render(request,'adminlogin.html')
def adminhome(request):
    if 'adm' in request.session:
        user=User.objects.all()
        return render(request,'adminhome.html',{'user':user})
    else:
        return redirect(index)
def adminlogout(request):
    if 'adm' in request.session:
        del request.session['adm']
        return redirect(adminlogin)
def userlogout(request):
        logout(request)
        return redirect(userlogin)
def userhome(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'userhome.html',{'user':user})
    else:
        return redirect(userlogin)
    
def userprofile(request):
    return render(request,'user_profile.html')
def leave_balance(request):
    return render(request,'user_leave_balance.html')
def userpayroll(request):
    return render(request,'user_payroll.html')
def userpayslips(request):
    return render(request,'user_payslips.html')
def usersupport(request):
    return render(request,'user_support.html')
