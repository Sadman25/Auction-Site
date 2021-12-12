from django.shortcuts import render
from .forms import productForm

# Create your views here.
def homePage(request):
    context = {}
    return render (request, 'homepage.html',context)

def createAuction(request):
    
    newProduct = productForm()
    
    context = {'newProduct':newProduct}
    return render (request, 'create_auction.html',context)