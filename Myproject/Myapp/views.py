from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

# def homepage(request):
#     return HttpResponse('Home page content')
def homepage(request):
    page={
        "tittle":"This is Arifen's Homepage",
        "content":"Welcome" 
    }
    return render(request,"index.html", context=page)

def contact(request):

    email="exmple@gmail.com"
    socail_profile=[
        "Facebook:facebook.com",
        "Instagram:instagram.com",
        "Youtube:youtube.com",
        "Github:github.com"
    ]
    HD ="C"
    return render(request,"contact.html", {"emailaddress":email , "socialprofile":socail_profile , "HD":HD})

def about(request):
    return render(request,"about.html")