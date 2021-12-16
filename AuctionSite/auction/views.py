from django.shortcuts import redirect, render
from .forms import productForm,imagesForm, biddingForm
from .models import product, images, bidding
from django.contrib.auth.models import User
from accounts.models import profile
from accounts.forms import userRegistration,profileRegistration
# Create your views here.
def homePage(request):
    products = product.objects.all().order_by('-id')
    context = {'products':products}
    return render (request, 'homepage.html',context)

def createAuction(request):
    
    newProduct = productForm()
    additionalImages= imagesForm()

    if request.method == 'POST':
        newProduct = productForm(request.POST,request.FILES)
        additionalImages= request.FILES.getlist('image')

        if newProduct.is_valid():
            product = newProduct.save(commit=False)
            product.owner = request.user
            product.save()

            for i in additionalImages:
                photo = images.objects.create(
                    product = product,
                    image = i
                )

            return redirect('homePage')

    else:
        context = {'newProduct':newProduct,
        'additionalImages':additionalImages }
        return render (request, 'create_auction.html',context)


def productDetails(request,pk):
    product_details = product.objects.get(id=pk)
    product_images = images.objects.filter(product=product.objects.get(id=pk))
    allBiddings = bidding.objects.filter(product=product.objects.get(id=pk))

    newBid = biddingForm()
    
    if request.method == 'POST':
        newBid = biddingForm(request.POST)
        if newBid.is_valid():
            newBid = newBid.save(commit=False)
            newBid.bidder = request.user
            newBid.product = product.objects.get(id=pk)
            newBid.save()
            return redirect('productDetails')

    context = {'product_details':product_details,
    'product_images':product_images,
    'newBid':newBid,
    'allBiddings':allBiddings,
    }
    return render (request,'product_details.html',context)

def editProduct(request,pk):
    product_details = product.objects.get(id=pk)
    editProduct = productForm(instance=product_details)

    if request.method == 'POST':
        editProduct = productForm(request.POST,request.FILES,instance=productDetails)
        if editProduct.is_valid():
            editProduct.save()
            return redirect ('productDetails')
    
    context = {'product_details':product_details,
    'editProduct':editProduct
    }
    return render (request,'product_edit.html',context)

def myPosts(request):
    products = product.objects.all()
    context = {'products':products}
    return render (request, 'myposts.html',context)


def myProfile(request,pk):

    previousInfo = profile.objects.get(id=pk)
    editUser = userRegistration(instance=request.user)
    editProfile = profileRegistration(instance=previousInfo)

    if request.method == 'POST':
        editUser = userRegistration(request.POST,instance=request.user)
        editProfile = profileRegistration(request.POST,request.FILES,instance=previousInfo)
        if editUser.is_valid() and editProfile.is_valid():
            editUser.save()
            editProfile.save()
            return redirect ('homePage')
    
    else:
        context = {'previousInfo':previousInfo,
        'editUser':editUser,
        'editProfile':editProfile}
        return render (request, 'myProfile.html',context)   