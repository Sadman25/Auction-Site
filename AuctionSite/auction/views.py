from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {}
    return render (request, 'homepage.html',context)

def createAuction(request):
    context = {}
    return render (request, 'homepage.html',context)