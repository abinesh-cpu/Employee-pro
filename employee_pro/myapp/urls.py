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
]
