from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('userlogin',views.userlogin),
    path('userregister',views.userregister),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('adminlogout',views.adminlogout),
    path('userhome',views.userhome),
    path('userlogout',views.userlogout),
    path('userprofile',views.userprofile),
    path('leavebalance',views.leave_balance),
    path('userpayroll',views.userpayroll),
    path('userpayslips',views.userpayslips),
    path('usersupport',views.usersupport),
    path('employees',views.admin_employees),
    path('leaverequests',views.admin_leaverequests),
    path('payroll',views.admin_payroll),
    path('reports',views.admin_reports),
    path('settings',views.admin_settings),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
]
