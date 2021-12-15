from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
# Create your models here.
class category (models.Model):
    category = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.category

class status (models.Model):
    status = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.status

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

class images(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.product.owner.username

class bidding(models.Model):
    bid = models.PositiveIntegerField(null=False, blank=False)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.product.product_name + ' '+self.bidder.username