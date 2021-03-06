# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import DateField
# Create your models here.

#Category model will hold the type of product.
class category (models.Model):
    category = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.category

#It will hold the information whether a product on auction is sold or bidding still going on
class status (models.Model):
    status = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.status

#product model and its fields. It will contain neccessary information about a product in auction.
class product(models.Model):
    product_name= models.CharField(max_length=50, blank=False)
    product_description=models.CharField(max_length=500,null=False, blank=False)
    cover_photo=models.ImageField(null=False, blank=False)
    starting_bid = models.PositiveIntegerField(null=False, blank=False)
    deadline = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product_status = models.ForeignKey(status, null=True, on_delete= models.SET_NULL)
    product_category = models.ForeignKey(category, null=True, on_delete= models.SET_NULL)

    def __str__(self) -> str:
        return 'Product: '+self.product_name + ' Owner: '+ self.owner.username

    def get_absolute_url(self):
        return reverse('productDetails', kwargs={'pk':self.id})

#images model will hold additional images of a particular product
class images(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.product.owner.username

#Bidding model will hold the bidding and bidder information of products.
class bidding(models.Model):
    bid = models.PositiveIntegerField(null=False, blank=False)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    time = models.DateTimeField(auto_now_add=True,null=False)

    def __str__(self):
        return self.product.product_name + ' '+self.bidder.username