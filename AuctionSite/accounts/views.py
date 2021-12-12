from django.shortcuts import render, redirect
from .forms import userRegistration,profileRegistration
# Create your views here.

def loginPage(request):
    return render (request,'loginpage.html')


def homePage(request):
    return render (request, 'homepage.html')


def registration(request):
    userForm = userRegistration()
    profileForm = profileRegistration()
    context = {
        'userForm':userForm,
        'profileForm':profileForm
    }
    return render (request,'registration.html',context)

