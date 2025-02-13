from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('userlogin',views.userlogin),
    path('userreg',views.userreg),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('adminlogout',views.adminlogout),
    path('userlogout',views.userlogout),
    path('userhome',views.userhome),
    
]
