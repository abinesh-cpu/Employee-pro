from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

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
def admin_employees(request):
    return render(request,'admin_employees.html')
def admin_leaverequests(request):
    return render(request,'admin_leaverequests.html')
def admin_payroll(request):
    return render(request,'admin_payroll.html')
def admin_reports(request):
    return render(request,'admin_reports.html')
def admin_settings(request):
    return render(request,'admin_settings.html')

# Password Reset Request View
def password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                return redirect('password_reset_done')

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())

            # Send email with reset link
            domain = get_current_site(request).domain
            link = f"http://{domain}/password_reset_confirm/{uid}/{token}/"
            subject = 'Password Reset Request'
            message = f'Click the link to reset your password: {link}'
            send_mail(subject, message, 'noreply@domain.com', [email])

            return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

# Password Reset Done View
def password_reset_done(request):
    return render(request, 'password_reset.html')

# Password Reset Confirm View
def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = CustomSetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = CustomSetPasswordForm(user)
        
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        return HttpResponse('The reset link is invalid or expired.', status=400)

# Password Reset Complete View
def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')