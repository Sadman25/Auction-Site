from django.shortcuts import redirect, render
from .forms import productForm,imagesForm
from .models import product, images
from django.forms import modelformset_factory
# Create your views here.
def homePage(request):
    context = {}
    return render (request, 'homepage.html',context)

def createAuction(request):
    
    newProduct = productForm()
    additionalImages = modelformset_factory(images, form=imagesForm,extra=3)

    if request.method == 'POST':
        newProduct = productForm(request.POST,request.FILES)
        imagesFormset = additionalImages(request.POST , request.FILES, queryset=images.objects.none())

        if newProduct.is_valid():
            product = newProduct.save(commit=False)
            product.owner = request.user
            product.save()

            for form in imagesFormset.cleaned_data:
                if form:
                    image = form['image']
                    photo = images(product=product, image=image)
                    photo.save()

            return redirect('homePage')

    else:
        context = {'newProduct':newProduct,
        'additionalImages':additionalImages }
        return render (request, 'create_auction.html',context)