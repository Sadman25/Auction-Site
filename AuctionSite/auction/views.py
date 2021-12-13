from django.shortcuts import redirect, render
from .forms import productForm,imagesForm
from .models import product, images
from django.forms import modelformset_factory
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
    context = {'product_details':product_details}
    return render (request,'product_details.html',context)


def myPosts(request):
    products = product.objects.all()
    context = {'products':products}
    return render (request, 'myposts.html',context)