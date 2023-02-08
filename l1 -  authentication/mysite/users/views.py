from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from  users.models import User_Detail
from django.contrib import auth, messages

# from django.contrib.auth import authenticate


# Create your views here.
def home(request):
    template_name='home.html'
    return render(request , template_name)


def register(request):
    if request.method =='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        
        if password1 != password2:
            print('incorect')
            messages.info(request, 'Incorect password please.....')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            print('Username exists')
            messages.info(request, 'Username exists.....')
            return redirect('register')
            
        else:
        
            user=User.objects.create_user(username=uname, email=email, password=password1)
            user.save()
            user2= User_Detail(user=user,username=uname, email=email)
            user2.save()
            messages.info(request, 'User  Created.....')
            
            print('user created')
            return redirect('login')
    
    
    
    
    
    
    
    template_name='register.html'
    return render(request , template_name)

def login(request):    
    if request.method =='POST':
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        
        user= auth.authenticate(username=uname, password=pass1)
        
        if User.objects.filter(username=uname).exists():           
        
            if user is not None:
                auth.login(request, user)
                print('login success')
                messages.info(request, 'Login  Success.....')
                return redirect('/')
            else:
                print('invalid details')
                messages.info(request, 'Invalid Password.....')
                return redirect('login')
        else:            
            print('Invalid username')
            messages.info(request, 'Invalid username.....')
            return redirect('login') 
        
    template_name='login.html'
    return render(request , template_name)



def logout(request):
    auth.logout(request)
    messages.info(request, "you're logged out")
    
    print("you're logged out")
    return redirect('login')