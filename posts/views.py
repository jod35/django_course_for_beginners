from django.http import HttpRequest
from django.shortcuts import render,redirect
from .forms import PostCreationForm
from .models import Post

# Create your views here.


def index(request:HttpRequest):
    posts=Post.objects.all()

    context={
        'posts':posts
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")


def create_post(request):
    form=PostCreationForm()

    if request.method =="POST":
        data= request.POST

        title= data["title"]
        content=data["content"]
        author=data["author"]

        new_post=Post(
            title=title,
            content=content,
            author=author
        )

        new_post.save()

        # return redirect('posts_home')


    context={
        'form':form
    }
    return render(request,'createpost.html',context)