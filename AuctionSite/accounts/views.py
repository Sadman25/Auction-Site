from django.shortcuts import render, redirect

# Create your views here.

def loginPage(request):
    return render (request,'loginpage.html')


def homePage(request):
    return render (request, 'homepage.html')


def registration(request):
    return render (request,'registration.html')

