from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email alreaddy used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Usename already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password does not match') 
            return redirect('register')   
    else:
        return render(request,'register.html')
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')



def Logout(request):
    auth.logout(request)
    return redirect('/')

# Authored by Arunkumar
