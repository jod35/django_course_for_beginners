from django.shortcuts import render,redirect
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.



def sign_up(request):
    form=UserRegistrationForm()

    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm=request.POST["confirm"]

        if password == confirm:
            new_user=User.objects.create_user(
                username=username,
                email=email
            )

            new_user.set_password(password)

            new_user.save()

            return redirect('posts_home')




    context={
        'form':form
    }
    return render(request,'users/signup.html',context)


def login_user(request):
    form=LoginForm()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('posts_home')
        

    context={'form':form}
    return render(request,'users/login.html',context)


def logout_user(request):
    logout(request)
    return redirect('posts_home')