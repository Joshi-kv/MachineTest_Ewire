from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from home.models import Profile
# Create your views here.

def signup(request):
    if request.method == 'POST' :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('user:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('user:signup')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                
                #creating new profile for logged user 
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('user:login')
        else :
            messages.info(request,"Password not matching")
            return redirect('user:signup')
            
    return render(request,'signup.html')


def login(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('home:index')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('user:login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('user:login')