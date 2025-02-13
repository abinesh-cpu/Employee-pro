from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request,'index.html')
from .models import *
# Create your views here.
users=[]
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        users.append({'username':username,'password':password})
        for i in users:
            if i['username']==username and i['password']==password:
                print("logged in successfully")
                users.append({'username':username,'password':password})
                return redirect(userhome)
    return render(request,'userlogin.html',{'user':user})
def userregister(request):
    if request.method=='POST':
        slno=len(users)
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        data=user.objects.create(username=username,email=email,password=password)
        users.append({'slno':slno+1,'username':username,'password':password,'email':email})
        print(users)
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
    return render(request,'userhome.html')


