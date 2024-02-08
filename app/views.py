from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Customeuser,Student,Sessionyear
# Create your views here.

def base(request):
    return render(request,'base.html')


def signin(request):
    return render(request,'login.html')

def dologin(request):
    if request.method=='POST':
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),
                                       password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_Type=user.user_Type
            if user_Type == '1':
                return redirect('home')
            elif user_Type == '2':
                return HttpResponse('This is staff panel')
            elif user_Type == '3':
                return HttpResponse('This is student panel')
            else:
                messages.error(request,'Email and password are invalid')
                return redirect('login')
        else:
            messages.error(request,'Email and password are invalid')

            return redirect('login')
        
@login_required(login_url='login')
def hodhome(request):
    return render(request,'hod/home.html')

def dologout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user=Customeuser.objects.get(id=request.user.id)
    context={
        'user':user
    }
    return render(request,'profile.html')

def profile_update(request):
    if request.method=='POST':
        profilepic=request.FILES.get('profilepic')
        firstname=request.POST.get('first')
        lastname=request.POST.get('last')
        username=request.POST.get('user')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        try:
            customeuser=Customeuser.objects.get(id=request.user.id)
            customeuser.first_name=firstname
            customeuser.last_name=lastname
            if password!=None and password!="":
                customeuser.set_password(password)   
            if profilepic !=None and profilepic != "":
                customeuser.profilepic=profilepic
            customeuser.save()      
            messages.success(request,'your profile update successfully')
            return redirect('profile')  
        except:
            messages.error(request,'failed to update your profile')
    return render(request,'profile.html') 

def addstudent(request):
    session=Sessionyear.objects.all()

    context={

        'session':session
    }
    if request.method== 'POST':
        profilepic=request.FILES.get('profilepic')
        firstname=request.POST.get('first')
        lastname=request.POST.get('last')
        username=request.POST.get('user')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        course=request.POST.get('course')
        sessionid=request.POST.get('sessionid')

        if Customeuser.objects.filter(email=email).exists():
            messages.warning(request,'email already taken')
            return redirect('addstudent')
        if Customeuser.objects.filter(username=username).exists():
            messages.warning(request,'username already taken')
            return redirect('addstudent')
        else:
            user=Customeuser(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                profilepic=profilepic,
                user_Type=3
            )
            user.set_password=password
            user.save()
            session=Sessionyear.objects.filter(id=sessionid)

            students=Student(
                admin=user,
                address=address,
                session_year_id=session,
                course=course,
                gender=gender
            )

            students.save()
            messages.success(request,'student successfully saved')
            return redirect('addstudent')
        
            
    return render(request,'hod/addstudent.html',context)