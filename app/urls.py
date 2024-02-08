from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.base,name='home'),
    path('login/',views.signin,name='login'),
    path('dologin/',views.dologin,name='dologin'),
    path('dologout/',views.dologout,name='dologout'),
    path('profile/',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profileupdate'),



# hod pannel url
    path("hod/home",views.hodhome, name="home"),
    path('hod/addstudent',views.addstudent,name='addstudent'),


]